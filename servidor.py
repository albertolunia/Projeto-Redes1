import socket

# Função para lidar com lances
def process_bid(item, new_bid):
    global items
    current_bid = items.get(item, 0)
    if new_bid > current_bid:
        items[item] = new_bid
        return "BID_ACCEPTED"
    else:
        return "BID_REJECTED"

# Função para lidar com solicitação de lista de itens
def get_item_list():
    item_list = ";".join([f"{item},{value}" for item, value in items.items()])
    return f"ITEM_LIST {item_list}"

# Configuração do servidor
HOST = '127.0.0.1'
PORT = 12345

# Dados iniciais
items = {'item1': 100, 'item2': 150}

# Configuração do socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Servidor ouvindo em {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            # Processa a mensagem do cliente
            if data == "LIST_ITEMS_REQUEST":
                response = get_item_list()
            elif data.startswith("BID"):
                _, item, new_bid = data.split()
                response = process_bid(item, int(new_bid))
            else:
                response = "INVALID_REQUEST"

            # Envia resposta de volta ao cliente
            conn.sendall(response.encode())

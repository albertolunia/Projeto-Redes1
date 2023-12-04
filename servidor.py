import socket
import time
import threading

# Função para lidar com lances
def process_bid(name, item_id, new_bid):
    global items, highest_bids
    item_names = list(items.keys())
    if 1 <= item_id <= len(item_names):
        item = item_names[item_id - 1]
        current_bid = items.get(item, 0)
        if new_bid > current_bid:
            items[item] = new_bid
            highest_bids[item] = (name, new_bid)  # Atualiza o maior lance para este item
            return f"\n{name} fez o lance com sucesso! ✔️ Lance Aceito"
        else:
            return f"\n{name}, seu lance foi recusado. ❌ Valor abaixo do lance atual"
    else:
        return "\n❗ ID do item inválido"

# Função para lidar com solicitação de lista de itens
def get_item_list():
    item_list = "\n".join([f"ID: {index} - Item: {item} - Valor: R${value}" for index, (item, value) in enumerate(items.items(), start=1)])
    return f"===== Leilão da Polícia Federal =====\n{item_list}\n======================"

# Função para lidar com um cliente
def handle_client(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        if data == "LIST_ITEMS_REQUEST":
            response = get_item_list()
        elif data.startswith("BID"):
            try:
                _, name, item_id, new_bid = data.split()
                response = process_bid(name, int(item_id), int(new_bid))
            except ValueError:
                response = "\n❗ Formato de lance inválido"
        else:
            response = "\n❗ INVALID REQUEST"

        conn.sendall(response.encode())

    conn.close()

# Configuração do servidor
HOST = '127.0.0.1'
PORT = 12345

# Dados iniciais
items = {'iPhone 13 Pro (128GB)': 4999, 'Laptop Dell XPS 15': 6499, 'Samsung Galaxy Tab S7+': 2299, 'NVIDIA GeForce RTX 3080': 1999}
highest_bids = {item: ("", 0) for item in items}  # Inicializa os maiores lances como vazio para cada item

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Servidor ouvindo em {HOST}:{PORT}")

    # Tempo limite para o leilão (exemplo de 1 minuto)
    tempo_limite = time.time() + 60  # 1 minuto em segundos

    while time.time() < tempo_limite:
        conn, addr = server_socket.accept()
        print(f"Conectado por {addr}")

        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()

    print("\nLeilão encerrado. Resultados finais:")
    for item, (name, bid) in highest_bids.items():
        if name != "":
            print(f"Item: {item} - Maior Lance por {name}: R${bid}")
        else:
            print(f"Item: {item} - Sem lances")
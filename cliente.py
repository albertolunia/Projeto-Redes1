import socket

# Configuração do cliente
HOST = '127.0.0.1'
PORT = 12345

# Função para solicitar e imprimir a lista de itens
def get_item_list(client_socket):
    client_socket.sendall("LIST_ITEMS_REQUEST".encode())
    data = client_socket.recv(1024).decode()
    print(data)

# Função para enviar um lance
def place_bid(client_socket, item, new_bid):
    message = f"BID {item} {new_bid}"
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024).decode()
    print(response)

# Configuração do socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        print("\nEscolha uma opção:")
        print("1. Ver lista de itens")
        print("2. Fazer um lance")
        print("3. Sair")

        choice = input("Opção: ")

        if choice == "1":
            get_item_list(client_socket)
        elif choice == "2":
            item = input("Digite o nome do item: ")
            bid = int(input("Digite o valor do lance: "))
            place_bid(client_socket, item, bid)
        elif choice == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")
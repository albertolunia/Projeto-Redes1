import socket

# Configuração do cliente
HOST = '10.0.0.152'
PORT = 12345

# Função para solicitar e imprimir a lista de itens
def get_item_list(client_socket):
    try:
        client_socket.sendall("LIST_ITEMS_REQUEST".encode())
        data = client_socket.recv(1024).decode()
        print(data)
    except ConnectionError as e:
        print(f"Erro de conexão: {e}")

# Função para enviar um lance
def place_bid(client_socket, name, item, new_bid):
    try:
        message = f"BID {name} {item} {new_bid}"
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        print(response)
    except (ValueError, ConnectionError) as e:
        print(f"Erro durante o lance: {e}")

# Configuração do socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
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
                try:
                    name = input("Digite seu nome: ")
                    item = input("Digite o ID do item: ")
                    bid = int(input("Digite o valor do lance: "))
                    place_bid(client_socket, name, item, bid)
                except ValueError:
                    print("Valor do lance inválido. Tente novamente.")
            elif choice == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")
    except ConnectionError as e:
        print(f"Erro de conexão: {e}")

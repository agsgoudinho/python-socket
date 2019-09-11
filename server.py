import socket

import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = sock.bind(('localhost', 9000))

sock.listen(1)

mensagem = "Hello client"
tamanho_da_mensagem = len(mensagem)
print("Tamanho da mensagem = {}".format(len(mensagem)))

while True:
    print("Aguardando conexao")
    connection, address_client = sock.accept()

    connection.sendall(str(tamanho_da_mensagem).zfill(4).encode())

    connection.sendall(mensagem.encode())
    while True:
        expected_data_size = ''

        while (expected_data_size == ''):
            expected_data_size += connection.recv(4).decode()
            expected_data_size = int(expected_data_size)
            received_data = ''

        while len(received_data) < expected_data_size:
            received_data += connection.recv(4).decode()
            print(received_data)

        #
        time.sleep(2)

        resp = input("servidor: ").strip()
        send_data_size = len(resp)
        connection.sendall(str(send_data_size).zfill(4).encode())
        connection.sendall(resp.encode())

        if received_data == 'see ya':
            connection.close()

    connection.close()
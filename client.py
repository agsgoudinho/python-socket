import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 9000))

try:
    while True:
        expected_data_size = int(sock.recv(4).decode())
        received_data = ''

        while len(received_data) < expected_data_size:
            received_data += sock.recv(4).decode()
            print(received_data)

        mensagem = input("cliente: ").strip()
        send_data_size = len(mensagem)
        sock.sendall(str(send_data_size).zfill(4).encode())

        sock.sendall(mensagem.encode())

        #
        time.sleep(3)

        if received_data == 'see ya':
            sock.close()

finally:
    sock.close()
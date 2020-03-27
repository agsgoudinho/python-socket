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

        if received_data.lower() == 'see ya':
            break

        time.sleep(2)

        mensagem = input("cliente: ").strip()
        send_data_size = len(mensagem)
        sock.sendall(str(send_data_size).zfill(4).encode())
        sock.sendall(mensagem.encode())

        if mensagem.lower() == "see ya":
            break

finally:
    sock.close()

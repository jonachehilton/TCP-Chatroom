import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDR = (SERVER, PORT)
FORMAT = "ascii"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

nickname = input("Choose a nickname: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(nickname.encode(FORMAT))
            else:
                print(message)

        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = input("")
        formatted_message = f'{nickname}: {message}'
        if message.startswith("/"):
            if message[1:4] == "who":
                client.send(message.encode(FORMAT))
            if message[1:3] == "pm":
                client.send(message.encode(FORMAT))

            else:
                print("Not a valid command")

        else:
            client.send(formatted_message.encode(FORMAT))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

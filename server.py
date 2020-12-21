import socket
import threading
import time

# Using local IP address as host
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDR = (SERVER, PORT)
FORMAT = "ascii"

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []


def get_time():
    return "{}:{}:{}".format(time.localtime()[3], time.localtime()[4], time.localtime()[5])


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)


# When a client does the /who command
def get_nicknames():
    string_of_nicknames = f"{threading.active_count() - 1} user/s in the chatroom: "
    for nickname in nicknames:
        if nickname != nicknames[-1]:
            string_of_nicknames += f"{nickname}, "
        else:
            string_of_nicknames += f"{nickname}"

    return string_of_nicknames


# Handling Messages From Clients
def handle(client, address):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            if message.decode(FORMAT) == "/who":
                client.send(get_nicknames().encode(FORMAT))
            else:
                broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode(FORMAT))
            nicknames.remove(nickname)
            print("\n{} [CONNECTION ENDED] Disconnected from {}/{}"
                  .format(get_time(), str(address[0]), str(address[1])))
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("\n{} [NEW CONNECTION] Joined from {}/{}".format(get_time(), str(address[0]), str(address[1])))

        # Request And Store Nickname
        client.send('NICK'.encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("\n{} [SET NICKNAME] New client's nickname is set to: {}".format(get_time(), nickname))
        broadcast("{} has joined the chatroom!".format(nickname).encode(FORMAT))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client, address))
        thread.start()


print("{} [SERVER STARTED]".format(get_time()))

receive()

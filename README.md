
# Client / Server TCP Chatroom

A TCP-based chat room consisting of a host server connected to a number of client servers through an IP address, port number, and nickname.

Note: this project is still under development.
## Host
The host server can connect to the socket and open the chat by executing the following command line.
```bash
$ python host.py
```
The host console prints all activity by users in the chat.

## Client
A client server can connect to the socket and enter the chat by executing the following command line.
The IP address and port number provided by the client must match those of the host in order for the handshake to succeed.
```bash
$ python client.py
```
All user commands are conducted through the console with a `/` character and executed by the `Enter` key. To send a message to all members of the chat, simply type text into the console.

PLANNED: To send a private message to another member, begin the message with an `@` symbol followed by the nickname of the recipient.
```
@jonache This is a special message
```
To query the chat for a list of all active usernames, type the `/who` command.
```
/who
```
A user can leave the chat with the `Ctrl+C` interrupt sequence.

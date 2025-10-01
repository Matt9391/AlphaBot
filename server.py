import socket
import AlphaBot

#Python DOCS

# 0.0.0.0 indirizzo ip speciale, anche detto This Host
ADDRESS = ("0.0.0.0", 6969)
BUFFER = 4096
                                #socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(ADDRESS)

#numero di connessioni possibili in coda
N = 1
s.listen(N)

ab = AlphaBot.AlphaBot()

actions = {
    'w' : ab.forward,
    'a' : ab.left,
    's' : ab.backward,
    'd' : ab.right
    }

connection, address = s.accept()
while True:

    #recv perché sappiamo già da dove
    data = connection.recv(BUFFER)
    act = data.decode()

    actions[act]()

    #invia messaggi al client
    connection.send("skibidi".encode())

s.close()


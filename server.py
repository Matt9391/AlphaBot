import socket
import AlphaBot
import GestoreSensori 

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
gs = GestoreSensori.GestoreSensori(ab)
gs.start()


actions = {
    'w' : lambda : ab.forward(),
    'a' : lambda : ab.left(),
    's' : lambda : ab.backward(),
    'd' : lambda : ab.right(),
    'e' : lambda : ab.changeSpeed(10, 10),
    'q' : lambda : ab.changeSpeed(-10, -10),
    'stop' : lambda : ab.stop()
    }

state = "stop"

connection, address = s.accept()
while True:

    #recv perché sappiamo già da dove
    data = connection.recv(BUFFER)
    act = data.decode()

    if act in actions and act != state:
        actions[act]()
        state = act

    #invia messaggi al client
    # connection.send("skibidi".encode())

s.close()


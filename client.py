import socket
from pynput import keyboard
#Python DOCS

# 0.0.0.0 indirizzo ip speciale, anche detto This Host
# ADDRESS = ("0.0.0.0", 5000)
SERVER_ADDRESS = ("192.168.1.57",6969)
BUFFER = 4096
                                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(SERVER_ADDRESS)



def on_press(key):
    try:
        if key.char == 'w':
            print("AVANZA")
            s.send('w'.encode())
        elif key.char == 'a':
            print("SINISTRA")
            s.send('a'.encode())
        elif key.char == 's':
            print("GIUUU")
            s.send('s'.encode())
        elif key.char == 'd':
            print("DESTRA")
            s.send('d'.encode())
    except AttributeError:
        # Per tasti speciali (es. invio, frecce, ecc.)
        if key == keyboard.Key.enter:
            s.send('Error'.encode())
            print("Hai premuto INVIO!")



while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    data = s.recv(BUFFER)
    print("Other: " + data.decode())


s.close()




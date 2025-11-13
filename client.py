import socket
import time
from pynput import keyboard
#Python DOCS

# 0.0.0.0 indirizzo ip speciale, anche detto This Host
# ADDRESS = ("0.0.0.0", 5000)
SERVER_ADDRESS = ("192.168.1.125",6969)
BUFFER = 4096
                                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(SERVER_ADDRESS)

lastChar = '-'

def on_press(key):
    global lastChar
    try:
        if key.char == lastChar:
            return
        lastChar = key.char
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
        elif key.char == 'q':
            print("+ velocitaaa")
            s.send('q'.encode())
        elif key.char == 'e':
            print("- velocitaaa")
            s.send('e'.encode())
        elif key.char == 'r':
            print("squareee")
            s.send('r'.encode())
    except AttributeError:
        # Per tasti speciali (es. invio, frecce, ecc.)
        if key == keyboard.Key.enter:
            s.send('Error'.encode())
            print("Hai premuto INVIO!")
    # time.sleep(1)

def on_release(key):
    global lastChar
    try:
        if key.char != 'u':
            lastChar = "-"
            print("Tasto rilasciato")
            s.send("stop".encode())
    except AttributeError:
        # Per tasti speciali (es. invio, frecce, ecc.)
        return
    


while True:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    data = s.recv(BUFFER)
    print("Other: " + data.decode())


s.close()




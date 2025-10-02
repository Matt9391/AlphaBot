# Project AlphaBot
Development of AlphaBot using Python and TCP connection

## Key commands:

- **'w'** : move forward
- **'a'** : move left
- **'s'** : move backward
- **'d'** : move right

> These commands are sent to the Alphabot through client-server connection in TCP

[Client.py](client.py)
```python
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
        elif key.char == 'q':
            print("+ velocitaaa")
            s.send('q'.encode())
        elif key.char == 'e':
            print("- velocitaaa")
            s.send('e'.encode())
    except AttributeError:
        # Per tasti speciali (es. invio, frecce, ecc.)
        if key == keyboard.Key.enter:
            s.send('Error'.encode())
            print("Hai premuto INVIO!")
    time.sleep(1)
```
---
## To Do
- [x] move per seconds
- [ ] move per distance

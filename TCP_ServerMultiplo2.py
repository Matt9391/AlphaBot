import socket
import threading

MAX_CLIENTS = 3 # Numero massimo di client simultanei accettati dal server

# Crea un semaforo che permette solo MAX_CLIENTS accessi contemporanei
client_semaphore = threading.Semaphore(MAX_CLIENTS)

# Funzione che gestisce la comunicazione con un singolo client
def handle_client(client_socket, address):
    print(f"Connesso: {address}")  # Stampa che un client si è connesso
    with client_socket:
        try:
            while True:  # Ciclo di ricezione dati continuo
                data = client_socket.recv(1024)       # Riceve fino a 1024 byte dal client
                if not data:  # Se il client chiude la connessione
                    break
                message = data.decode().strip()  # Decodifica il messaggio
                print(f"[{address}] {message}")  # Stampa il messaggio ricevuto
                # Per rispondere al client:
                # client_socket.sendall(b"Messaggio ricevuto.\n")
        except Exception as e:
            print(f"Errore con {address}: {e}")  #Stampa l’errore
        finally:
            print(f"Disconnesso: {address}")  #Avvisa che il client si è disconnesso
            client_semaphore.release()  #Libera uno slot nel semaforo

# Funzione che avvia il server TCP
def start_server(host='0.0.0.0', port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server in ascolto su {host}:{port} (max {MAX_CLIENTS} client)")

    try:
        while True:
            client_socket, addr = server.accept()
            if client_semaphore.acquire(blocking=False):
                thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
                thread.start()
            else:
                print(f"Connessione rifiutata da {addr} (troppi client)")
                client_socket.sendall(b"Server occupato. Riprova piu' tardi.\n")
                client_socket.close()
    except KeyboardInterrupt:
        print("\nServer arrestato manualmente.")
    finally:
        server.close()


if __name__ == "__main__": 
    start_server()

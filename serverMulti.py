import socket
#Python DOCS
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_semaphore = 

def start_client(host= "127.0.0.0", port = 5000):
    print("sono uno")
    # with socket.socket(socket.af)    
def start_server(host = "0.0.0.0", post=5000):
    try:
        while True:
            client_socket, addr = server.accept()
            if(client_semaphore.acquire(blocking = False)):
                thread = threading.Thread(target=handle_client, args=(client_socket, addr))
                thread.start()
            else:
                print("connessione rifutata") 
                client_socket.sendall("server occupato")
                client_socket.close()
    except KeyboardInterrupt:
        print("arresto")
    finally:
        server.close()           


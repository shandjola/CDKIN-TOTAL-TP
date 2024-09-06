import socket 
import time
import threading
# Créer un socket 

def canal() :
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Connecter le socket au serveur 
    server_addr = ('192.168.164.129',80)
    sock.connect(server_addr)
    print("*")
    # Envoyer une requete au serveur 
    request = b'GET / HTTP/1.1\r\nHost:localhost\r\n\r\n'
    sock.sendall(request)

    #recevoir la réponse du serveur avec une latence de 10 millisecondes 
    reponse = b''
    while True :
        data = sock.recv(1024)
        if not data :
            break 
        time.sleep(0.01)
        reponse += data         
    print(reponse.decode())
    sock.close()
  
for _ in range(4000):
    t = threading.Thread(target=canal)
    t.start()


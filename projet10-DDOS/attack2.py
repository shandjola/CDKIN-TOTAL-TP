import requests
import threading      
# Créer une session persistante
def canal() :
    session = requests.Session()

    # Définir les paramètres de connexion
    url = "http://35.162.83.99/"
    while True :
        # Effectuer une première requête
        response = session.get(url)
        print(f"Statut de la première requête: {response.status_code}")
    
threads = []

for _ in range(20):
    t = threading.Thread(target=canal)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
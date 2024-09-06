import psutil
import csv
import datetime
import time 

# Définir le chemin du fichier CSV
csv_file = "/home/ec2-user/journal.csv"


def ecriture():
    # Ouvrir le fichier CSV en mode écriture
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Vérifier si le fichier est vide (première exécution)
        if file.tell() == 0:
            # Écrire l'en-tête du fichier CSV
            writer.writerow(["Timestamp", "Utilisation CPU (%)"])

        # Récupérer le pourcentage d'utilisation du CPU
        cpu_percent = psutil.cpu_percent(interval=1)

        # Obtenir l'heure actuelle
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Écrire les données dans le fichier CSV
        writer.writerow([timestamp, cpu_percent])

        print(f"Pourcentage d'utilisation du CPU : {cpu_percent}%")
        print(f"Données enregistrées dans {csv_file}")
        

while True :
    ecriture()
    time.sleep(2)
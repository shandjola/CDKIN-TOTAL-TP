#!/bin/bash 
# installation de pip pour gerer les packages
sudo yum -y install python3-pip 

# installation du module psutil de pythonn pour gerer le monitoring des ressources
pip install psutil

# Creation du fichier journal.csv
touch journal.csv 
# Rajout des permissions d'ecriture 
sudo chmod +w journal.csv

# creation du fichier performance.py pour l'enregistrement des performances 
sudo nano performance.py

# Execution du code python en background
python3 performance.py &

# Monitoring du fichier csv
tail -f journal.csv
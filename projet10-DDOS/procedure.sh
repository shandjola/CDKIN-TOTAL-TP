#!/bin/bash 
#Preparation de la machine de l'attaquant 
# Creation du fichier python pour l'attaque et on insère le code dessus
# Le fichier que nous avons ecrit dans le serveur est le fichier attack4(optimal).py 
# Attention : ce code est tres malveillant 
sudo nano attack.py
# Execution du script python 
python3 attack.py
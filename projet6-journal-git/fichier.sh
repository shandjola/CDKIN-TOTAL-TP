#!/bin/bash

# on verifie si le bay est present 
if [ -f "/etc/server.conf" ];
then 
    echo "$(date) => Fichier trouvé dans etc" 
else
    #Telecharger le fichier depuis git 
    echo "$(date) => Lancement du telechargement"
    git clone https://github.com/juniormeme/tp-cohorte.git
    # On recupère ce qui est le plus interessant
    sudo cp /home/ec2-user/tp-cohorte/server.conf /etc/server.conf
    sudo rm -r /home/ec2-user/tp-cohorte/
    echo "$(date) => Fichier server.conf telecharge"
fi

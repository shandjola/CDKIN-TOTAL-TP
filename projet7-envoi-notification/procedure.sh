#On est dans amazon linux 
#Voici les actions que nous avons effectué
# Installation de pip pour gerer les packets de python
sudo yum -y install python3-pip
# Installation de psutil pour monitorer le tout 
sudo pip install psutil 
# Creation du script python pour recuperer les ressources et l'envoyer par mail
sudo nano code.py
# Installation de crontab pour rendre une routine 
sudo yum -y install cronie
# Activation de crontab 
sudo systemctl start crond
# On ajout l'envoie des mails dans le crontab 
crontab -e
# On monitore le journal d'envoie de mail 
cd ~
tail -f -n 1 journal.log

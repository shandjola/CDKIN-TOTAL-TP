#On est dans amazon linux 
#Voici les actions que nous avons effectué
# Installation de git 
sudo yum -y install git 
# On se rassure qu'on est dans le home directory 
cd ~
# On edite le code du fichier
sudo nano fichier.sh
# on met les permissions necessaires pour l'execution
chmod o+x fichier.sh
# On installe crontab et l'active 
sudo yum -y install cronie
sudo systemctl start crond
# On rajoute la tache cron 
crontab -e

# on monitore le resultat
tail -f journal.log 


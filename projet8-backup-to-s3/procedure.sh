#On est dans amazon linux 
#Voici les actions que nous avons effectué
#Creaion des fichiers à mettre dans le bureau 
touch junior.txt junior2.txt  
#Creation et ecriture du code à executer 
sudo nano code.sh
#Ajout de la permission d'executer 
sudo chmod +x code.sh
# Installation et activaion du crontab 
sudo yum -y install cronie 
sudo systemctl start crond 
# Ecriture de la tache cron 
crontab -e 
# Monitoring du log 
tail -f journal.log

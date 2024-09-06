#On est dans amazon linux 
#Voici les actions que nous avons effectué
# On install et active cron 
sudo yum -y install cronie
systemctl start crond
# on verifie la liste
crontab -l
# on edite le fichier qui contient le code 
nano fichier.sh
# on met les permissions necessaires pour l'execution
chmod o+x fichier.sh
# on edite la tache cron 
crontab -e
# on monitore le resultat
tail -f journal-cron.log
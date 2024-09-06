#On est dans amazon linux 
#Voici les actions que nous avons effectué
# On install curl 
sudo yum -y install curl
# On edite le fichier qui va recevoir le code 
nano fichier.sh
# On rajoute la tache cron pour chaque minute
crontab -e
# On monitore le tout 
tail -f -n 1 journal-cron.log


#Installer et activer httpd : pour le serveur web
sudo yum -y install httpd 
sudo systemctl start httpd

#Installer et activation automatique de php 
sudo yum -y install php php-cli

#Ecrire le code et le placer dans /var/www/html/ 
cd /var/www/html
# On code le site
sudo nano index.php
# On code le site et on y insère le message de journalisation
sudo nano help.php

#Restart le httpd 
sudo systemctl restart httpd

#Journaliser le tout dans mon journal en background
sudo tail -f -n 1 /var/log/php-fpm/www-error.log >> /home/ec2-user/journal-php.log &

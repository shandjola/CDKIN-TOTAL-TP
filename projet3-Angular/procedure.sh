
# Installer curl 
sudo yum -y install curl
# Procedure d'installation de node.js 
# installs fnm (Fast Node Manager)
curl -fsSL https://fnm.vercel.app/install | bash
source /home/ec2-user/.bashrc
# download and install Node.js
fnm use --install-if-missing 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.15.0`

# verifies the right NPM version is in the environment
npm -v # should print `10.7.0`

#on revient au home 
cd ~
# On install angular avec npm 
npm install -g @angular/cli
# On voit la verion de angular qui est installé 
ng version 
# On crée un nouveau projet nommé tp
ng new tp 
# On entre dans le dossier tp (dossier du projet)
cd tp 
# On crée deux composants pour les pages "/home" et "/aide"
ng generate component home
ng generate component aide
# On se place dans le dossier src/app/home/ pour editer le fichier home.component.ts
cd src/app/home
# On edite le fichier pour inserer le code 
sudo nano home.component.ts
# on rentre d'un dossier en arrière 
cd ..
# on entre dans le dossier aide 
cd aide 
# edite le fichier aide.component.ts
sudo nano aide.component.ts 
# on rentre d'un dossier qui est le dossier app 
cd ..
# on edite le fichier app.routes.ts
sudo nano app.routes.ts
# une fois terminé, on lance le serveur et on journalise les erreurs
# et on lance le serveur en background  
ng serve >> journal.log & 



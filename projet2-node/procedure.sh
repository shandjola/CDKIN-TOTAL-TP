
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
# on install la bibliotechque express
npm install express
# on cree le fichier server.js qui va comporter le serveur 
nano server.js
# on lance le serveur en background + la journalisation
node server.js >> journal.log & 
# on monitore le journal 
tail -f journal.log 

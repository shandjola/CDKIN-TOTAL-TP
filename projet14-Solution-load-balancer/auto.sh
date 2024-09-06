#!/bin/bash 
# on cree un dossier temporaire 
cd /home/ec2-user/notre-site/; mkdir temp
cd temp
# on entre dans temp 
# Telecharger le fichier 
git clone https://github.com/juniormeme/tp-cohorte.git
# Soutirer le fichier index.html 
cp ~/notre-site/temp/tp-cohorte/projet2-node/index.html /home/ec2-user/notre-site/temp/index.html
rm -rf tp-cohorte/
#
# Comparer les fichiers correspondants
diff ~/notre-site/index.html ~/notre-site/temp/index.html
if [ $? -eq 0 ]; then
    echo "$(date) : Pas de différence pour le fichier "
else
    echo "$(date) : Différences détectées pour le fichier : Mise à jour en cours"
    rm ~/notre-site/index.html
    mv index.html ~/notre-site/index.html
    cd ..
    rm -rf temp/
    # On rajoute le host name 
    sed -i "s/nom-du-serveur/$(hostname)/g" ~/notre-site/index.html
fi


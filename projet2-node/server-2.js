const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Définir le chemin vers le répertoire des fichiers statiques
app.use(express.static(path.join(__dirname, '/home/ec2-user/')));

// Définir la route pour renvoyer le fichier HTML
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Serveur démarré sur le port ${port}`);
});
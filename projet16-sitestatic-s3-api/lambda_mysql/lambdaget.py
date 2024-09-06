import mysql.connector
import json

def myfonction():
    # Connexion à la base de données MySQL
    db = mysql.connector.connect(
        host="44.203.91.22",
        port=3306,
        user="lambda",
        password="password",
        database="cohorte"
    )

    # Création d'un curseur
    cursor = db.cursor()

    # Requête SQL pour récupérer les données
    query = "SELECT * FROM user"
    cursor.execute(query)

    # Récupération des résultats
    results = cursor.fetchall()
    print(results)
    
myfonction()
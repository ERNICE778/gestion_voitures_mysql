import mysql.connector
import json
from Voiture import Voiture

def connecter_db():
    with open("config.json") as  f:
        config = json.load(f)
    
    connexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )   

    return connexion

def creer_table():
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voiture (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marque VARCHAR(50),
        modele VARCHAR(50),
        annee INT,
        prix DECIMAL(10,2)
    )
    """)

    conn.commit()
    conn.close()


def ajouter_voiture(voiture):
    conn = connecter_db()
    cursor = conn.cursor()

    creer_table()

    cursor.execute(
        "INSERT INTO voiture (marque, modele, annee, prix) VALUES (%s, %s, %s, %s)",
        (voiture.marque, voiture.modele, voiture.annee, voiture.prix)
    )

    conn.commit()
    conn.close()    





def recuperer_voitures():
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM voiture")
    rows = cursor.fetchall()

    voitures = []
    for r in rows:
        voitures.append(Voiture(r[1], r[2], r[3], r[4], r[0]))

    conn.close()
    return voitures    



def supprimer_voiture(id):
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM voiture WHERE id = %s", (id,))

    conn.commit()
    conn.close()


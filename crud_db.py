import mysql.connector
import json

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


from Voiture import Voiture
from crud_db import connecter_db

conn = connecter_db()
print("connexion reussie")
conn.close()
    
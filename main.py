from Voiture import Voiture
from crud_db import connector_db

conn = connector_db()
print("connexion reussie")
conn.close()
    
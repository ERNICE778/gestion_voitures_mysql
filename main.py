from Voiture import Voiture
from crud_db import *

conn = connecter_db()
print("connexion reussie")
conn.close()
    

v = Voiture("Toyota", "Corolla", 2020, 20000)
ajouter_voiture(v)




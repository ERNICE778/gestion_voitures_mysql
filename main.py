from Voiture import Voiture
from crud_db import *

conn = connecter_db()
print("connexion reussie")
conn.close()
    

# v = Voiture("Toyota", "Corolla", 2020, 20000)
# ajouter_voiture(v)

supprimer_voiture(1)


voitures = recuperer_voitures()

for v in voitures:
    v.afficher_voiture()
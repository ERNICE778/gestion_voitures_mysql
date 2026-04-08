from Voiture import Voiture
from crud_db import *

conn = connecter_db()
print("connexion reussie")
conn.close()
    

v1 = Voiture("mercedes", "Corolla", 2020, 20000)
v2 = Voiture("yaris", "Corolla", 2024, 20000)

ajouter_voiture(v1)
ajouter_voiture(v2)







supprimer_voiture(7)



voitures = recuperer_voitures()

for v in voitures:
    v.afficher_voiture()

# modifier les infos d une voiture 
v2.marque = "jetour"
v2.modele ="evolution 2045"
v2.annee=2025
v2.prix=20200
v2.id=4
modifier_voiture(v2)

from Voiture import Voiture
from crud_db import *

conn = connecter_db()
print("connexion  a la base de donnees reussie")
conn.close()
    

v1 = Voiture("Tesla", "Model 3", 2025 , 55000)
v2 = Voiture("Kia", "Sportage", 2026, 31000)
v3=Voiture("Subaru","Crosstrek",2026,35000)
v4=Voiture("Volkswagen","golf GTI",2025,38000)

ajouter_voiture(v1)
ajouter_voiture(v2)
ajouter_voiture(v3)
ajouter_voiture(v4) 


#suppresion de la voiture ayant l id 20
supprimer_voiture (20)


voitures=recuperer_voitures()
for v in voitures:
    v.afficher_voiture()



# modifier les infos d une voiture ayant l id 23
v4.marque = "Mazda"
v4.modele ="CX-5"
v4.annee=2025
v4.prix=32000
v4.id=23
modifier_voiture(v4)

Class Voiture:
    def __init__(self,id=None,marque,modele,annee,prix):
        self.id=id
        self.marque=marque
        self.modele=modele
        self.annee=annee
        self.prix=prix


    def afficher_voiture(self):
        print(f"ID:{self.id},marque :{self.marque},annee: {self.annee}, prix: {self.prix}")    



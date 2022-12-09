"""
Crée par Lucas Tessier
Groupe 402
"""


class Rectangle:
    def __init__(self):
        self.largeur = 0
        self.longeur = 0
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.longeur * self.largeur
    def afficher_infos(self):
        print(f"Longeur: {self.longeur}")
        print(f"Largeur: {self.largeur}")
        print(f"Aire: {self.aire}")


r = Rectangle()
r.longeur = 10
r.largeur = 2
r.calcul_aire()
r.afficher_infos()
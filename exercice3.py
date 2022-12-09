"""
Créer par Lucas Tessier
Groupe 402
"""

from math import pi
class Cercle:
    def __init__(self):
        self.rayon = 0
        self.aire = 0
        self.circonference = 0
    def calcul_aire(self):
        self.aire = self.rayon**2 * pi
    def calcul_circonference(self):
        self.circonference = 2 * self.rayon * pi
    def afficher_infos(self):
        

c = Cercle()
c.rayon = 5
c.calcul_aire()
c.calcul_circonference()

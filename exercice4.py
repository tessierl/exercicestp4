"""
Créer par Lucas Tssier
Groupe 402
"""

import random

class Hero():
    def __init__(self):
        self.pv = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)
        self.nom = ""
    def afficher_combat(self):
        print(f"Vous êtes {self.nom} et vous avez affronté un monstre!")
        print(f"PVs: {self.pv}")
        print(f"Force d'attaque: {self.force_attaque}")
        print(f"Force de défense: {self.force_defense}")
        print("")
    def combat(self):
        self.attaque = self.force_attaque + random.randint(1, 6)
    def dommages(self, dommage):
        self.pv -= dommage - self.force_defense
    def afficher_combat2(self):
        print(f"Vous êtes {self.nom} et vous avez affronté un monstre!")
        print(f"PVs: {self.pv}")
        print(f"Force d'attaque: {self.force_attaque}")
        print(f"Force de défense: {self.force_defense}")
        print("")
        print()



h = Hero()
h.nom = "Kévun Tremblay"
h.afficher_combat()
h.combat()
h.dommages(5)
h.afficher_combat2()
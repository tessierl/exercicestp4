"""
Créer par Lucas Tessier
Groupe 402
"""

import random


class Hero:
    def __init__(self):
        self.pv = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)
        self.nom = ""

    def afficher_combat(self):
        print(f"Vous êtes {self.nom} et vous allez affronter un monstre!")
        print(f"PVs: {self.pv}")
        print(f"Force d'attaque: {self.force_attaque}")
        print(f"Force de défense: {self.force_defense}")
        print("")

    def combat(self):
        return self.force_attaque + random.randint(1, 6)

    def dommages(self, dommage):
        self.pv -= max(dommage - self.force_defense, 0)

    def afficher_combat2(self):
        print(f"Vous êtes {self.nom} et vous avez affronté un monstre!")
        print(f"PVs: {self.pv}")
        print(f"Force d'attaque: {self.force_attaque}")
        print(f"Force de défense: {self.force_defense}")
        print("")

    def est_vivant(self):
        if self.pv < 0:
            print("Tu est mort")
            return False
        elif self.pv > 0:
            return True


boucle = True
h = Hero()

while boucle:
    h.nom = "Kévun Tremblay"
    h.afficher_combat()
    h.combat()
    h.dommages(5)
    h.afficher_combat2()
    if not h.est_vivant():
        print("Tu est mort :(")
        boucle = False

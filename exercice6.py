"""
Créer par Lucas Tessier
Groupe 402
"""

from dataclasses import dataclass
import random


@dataclass
class Hero:
    nom: str
    pv: int
    force_attaque: int
    force_defense: int


class Aventure:
    def __init__(self):
        self.nom = ""
        self.stats = Hero("Kévun Tremblay", random.randint(1, 10) + random.randint(1, 10), random.randint(1, 6),
                          random.randint(1, 6))

    def afficher_combat(self):
        print(f"Vous êtes {self.stats.nom} et vous allez affronter un monstre!")
        print(f"PVs: {self.stats.pv}")
        print(f"Force d'attaque: {self.stats.force_attaque}")
        print(f"Force de défense: {self.stats.force_defense}")
        print("")

    def combat(self):
        return self.stats.force_attaque + random.randint(1, 6)

    def dommages(self, dommage):
        self.stats.pv -= max(dommage - self.stats.force_defense, 0)

    def afficher_combat2(self):
        print(f"Vous êtes {self.stats.nom} et vous avez affronté un monstre!")
        print(f"PVs: {self.stats.pv}")
        print(f"Force d'attaque: {self.stats.force_attaque}")
        print(f"Force de défense: {self.stats.force_defense}")
        print("")

    def est_vivant(self):
        if self.stats.pv < 0:
            return False
        elif self.stats.pv > 0:
            return True


boucle = True
a = Aventure()

while boucle:
    a.nom = "Kévun Tremblay"
    a.afficher_combat()
    a.combat()
    a.dommages(random.randint(1, 7))
    a.afficher_combat2()
    if not a.est_vivant():
        print("Tu est mort :(")
        boucle = False

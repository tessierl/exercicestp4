#Crée par Lucas Tessier
#Groupe 402

from dataclasses import dataclass
import random

@dataclass
class Statsperso():
    force: int
    dexterite: int
    constitution: int
    intelligence: int
    sagesse: int
    charisme: int

class Test():
    def __init__(self):
        self.stats = Statsperso(random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))

t = Test()
print(f"Notre joueur a une force de {t.stats.force}")
print(f"Notre joueur a une dextérité de {t.stats.dexterite}")
print(f"Notre joueur a une constitution de {t.stats.constitution}")
print(f"Notre joueur a une intelligence de {t.stats.intelligence}")
print(f"Notre joueur a une sagesse de {t.stats.sagesse}")
print(f"Notre joueur a un charisme de {t.stats.charisme}")

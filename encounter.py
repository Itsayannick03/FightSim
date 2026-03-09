from fighter import Fighter
from move import Move
import random

class Encounter:
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self. fighter2 = fighter2
        
        self.attacker = None
        self.defender = None
        
        self.description = None
        
    def resolve_initiative(self):
        fighter1_initiative_score = self.fighter1.initiative + random.randint(-5, 5)
        fighter2_initiative_score = self.fighter2.initiative + random.randint(-5, 5)
        
        if fighter1_initiative_score == fighter2_initiative_score:
            self.attacker = None
            self.defender = None
        elif fighter1_initiative_score > fighter2_initiative_score:
            self.attacker = self.fighter1
            self.defender = self.fighter2
        else:
            self.attacker = self.fighter2
            self.defender = self.fighter1
            
    def run(self):
        self.fighter1.update_status()
        self.fighter2.update_status()
        
        self.resolve_initiative()
        
        if self.attacker == None or self.defender == None:
            self.description = "The fighters circle each other"
            return
        
        move = self.attacker.get_move()
        if self.attacker.attack_hits(self.defender, move):
            damage = self.attacker.calculate_damage(move)
            self.defender.take_damage(damage)
            self.description = f"{self.attacker.name} lands a {move.name} on {self.defender.name}"
        else:
            self.description = f"{self.attacker.name} misses a {move.name}."
  

ali = Fighter("Ali", 100, 50, 100, 100, 50, 0)
tyson = Fighter("Tyson", 120, 40, 120, 80, 40, 0)            
for _ in range(5):
    encounter = Encounter(ali, tyson)
    encounter.run()
    print(encounter.description)
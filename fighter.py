import random
from move import Move
class Fighter:
    def __init__(self, name, max_health = 100, accuracy = 50, strength = 100, stamina = 100, defense = 50, aggression = 0):
        self.name = name

        self.__max_health = max_health # avarage = 100
        self.current_health = max_health

        self.__max_stamina = stamina # avarage = 100
        self.current_stamina = stamina
        
        self.__max_accuracy = accuracy # avarage = 50 "hits 50% of their punches"
        self.current_accuracy = accuracy

        self.__max_strength = strength # avarage = 100
        self.current_strength = strength

        self.__max_defense = defense # avarage = 50 "blocks 50% of their punches"
        self.current_defense = defense

        self.max_initiative = 100 + aggression
        self.initiative = self.max_initiative

        self.momentum = 0
        
    

    def update_status(self):
        #recalculate stats based on stamina and damage, stamina weighs more than damage
        stamina_ratio = self.current_stamina / self.__max_stamina
        health_ratio = self.current_health / self.__max_health

        fatigue_mod = (0.8*stamina_ratio) + (0.2*health_ratio)
        power_mod = 0.7 + 0.3 * fatigue_mod

        self.current_accuracy = round(self.__max_accuracy * fatigue_mod)
        self.current_strength = round(self.__max_strength * power_mod)

        self.current_defense = round(self.__max_defense * fatigue_mod)

        # Reload initiative and depleate momentum
        

        self.max_initiative = round(self.initiative * fatigue_mod)
        if self.initiative > self.max_initiative:
            self.initiative = self.max_initiative
        
        if self.initiative < self.max_initiative:
            self.initiative += 1

        if self.momentum > 0:
            self.momentum -= 1
        elif self.momentum < 0:
            self.momentum = 0
        self.initiative += self.momentum
        
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Health: {self.current_health} / {self.__max_health}\n"
            f"Stamina: {self.current_stamina}"
        )
    

    # Combat
    def is_knocked_out(self):
        return self.current_health <= 0

    def take_damage(self, amount):
        self.current_health -= amount
        self.current_stamina -= 1
        self.initiative -= 4

        if self.current_health < 0:
            self.current_health = 0
        if self.current_stamina < 0:
            self.current_stamina = 0
        if self.initiative < 0:
            self.initiative = 0
     
    def attack_hits(self, opponent, move: Move):
        attack_score = random.randint(-10, 10) + self.current_accuracy + move.accuracy_mod
        defense_score = random.randint(-10, 10) + opponent.current_defense

        
        if attack_score > defense_score:
            self.current_stamina -= move.stamina_cost_hit
            if self.momentum < 10:
                self.momentum += 1
            return True
        else:
            self.current_stamina -= move.stamina_cost_miss
            self.momentum -= 3
            
            return False

    def hit(self, move):
        min_dmg = round(move.base_damage * 0.5)
        max_dmg = round(move.base_damage * 2)
        damage_mod = self.current_strength / 100

        damage = round(random.randint(min_dmg, max_dmg) * damage_mod)

        return damage

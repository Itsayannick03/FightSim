import random
from move import Move
from moves import jab, straight, hook, uppercut

class Fighter:
    def __init__(self, name, max_health = 100, accuracy = 50, strength = 100, stamina = 100, defense = 50, aggression = 0):
        self.name = name

        self.__max_health = max_health # avarage = 100
        self.current_health = max_health

        self.__max_accuracy = accuracy # avarage = 50 "hits 50% of their punches"
        self.current_accuracy = accuracy

        self.__max_strength = strength # avarage = 100
        self.current_strength = strength

        self.__max_defense = defense # avarage = 50 "blocks 50% of their punches"
        self.current_defense = defense


        self.max_initiative = 100 + aggression
        self.initiative = self.max_initiative
        
        self.__max_stamina = stamina # avarage = 100
        self.current_stamina = stamina

        self.momentum = 0
        
        self.moves = [jab, straight, hook, uppercut]
        self.moves_weight = [50, 25, 15, 10]
        
    

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
        
        self.drift_momentum()
        self.regenerate_stamina()
 
    # Momentum functions
    def drift_momentum(self):
        if self.momentum > 0:
            self.momentum -= 1
        elif self.momentum < 0:
            self.momentum += 1
    def increase_momentum(self, ammount):
        if self.momentum + ammount < 10:
            self.momentum += ammount
        else:
            self.momentum = 10
    def decrease_momentum(self, amount):
        if self.momentum - amount > -10:
            self.momentum -= amount
        else:
            self.momentum = -10
    # Stamina functions      
    def regenerate_stamina(self):
        if self.current_stamina < self.__max_stamina:
            self.current_stamina += 1
    def decrease_stamina(self, amount):
        if self.current_stamina + amount > 0:
            self.current_stamina -= amount
        else:
            self.current_stamina = 0
    # Initiative functions      
    def increase_initiative(self, amount):
        if self.initiative + amount < self.max_initiative:
            self.initiative += amount
        else:
            self.initiative = self.max_initiative
    def decrease_initiative(self, amount):
        if self.initiative - amount > 0:
            self.initiative -= amount
        else:
            self.initiative = 0
    
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
        
        self.decrease_stamina(1)
        self.decrease_initiative(4)
        self.decrease_momentum(2)
       
     
    def attack_hits(self, opponent, move: Move):
        attack_score = random.randint(-10, 10) + self.current_accuracy + move.accuracy_mod
        defense_score = random.randint(-10, 10) + opponent.current_defense

        
        if attack_score > defense_score:
            self.decrease_stamina(move.stamina_cost_hit)
            self.increase_momentum(1)
            
            return True
        else:
            self.decrease_stamina(move.stamina_cost_miss)
            self.decrease_momentum(2)
            
            return False

    def calculate_damage(self, move):
        min_dmg = round(move.base_damage * 0.5)
        max_dmg = round(move.base_damage * 2)
        damage_mod = self.current_strength / 100

        damage = round(random.randint(min_dmg, max_dmg) * damage_mod)

        return damage
    
    def get_move(self):
        move = random.choices(self.moves, weights=self.moves_weight, k=1)[0]
        return move

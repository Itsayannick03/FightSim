import random
class Fighter:
    def __init__(self, name, max_health, punch_accuracy, punch_damage, defense):
        self.name = name
        self.max_health = max_health #100
        self.current_health = max_health
        
        self.punch_accuracy = punch_accuracy #50
        self.punch_damage = punch_damage 

        self.defense = defense #40
        
    def take_damage(self, amount):
        self.current_health -= amount

        if self.current_health < 0:
            self.current_health = 0

    def punch(self, opponent):
        attack_score = random.randint(-10, 10) + self.punch_accuracy
        defense_score = random.randint(-10, 10) + opponent.defense

        if attack_score > defense_score:
            return True
        return False

        
  
    def is_knocked_out(self):
        return self.current_health <= 0

    def reset(self):
        self.current_health = self.max_health

    def __str(self):
        return(
            f"{self.name}\n"
            f"Health: {self.current_health}/{self.max_health}\n"
            f"Punch: {self.punch}\n"
            f"Kick: {self.kick}\n"
            f"Defense: {self.defense}"
        )
        

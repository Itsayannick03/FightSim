import random

from move import Move
from moves import jab, straight, hook, uppercut


class Fighter:
    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------
    def __init__(
        self,
        name,
        max_health=100,
        accuracy=50,
        strength=100,
        stamina=100,
        defense=50,
        aggression=0
    ):
        self.name = name

        # Base and current combat stats
        self.max_health = max_health  # average = 100
        self.current_health = max_health

        self.max_accuracy = accuracy  # average = 50
        self.current_accuracy = accuracy

        self.max_strength = strength  # average = 100
        self.current_strength = strength

        self.max_defense = defense  # average = 50
        self.current_defense = defense

        # Initiative and stamina
        self.max_initiative = 100 + aggression
        self.initiative = self.max_initiative

        self.max_stamina = stamina  # average = 100
        self.current_stamina = stamina

        # Short-term fight flow
        self.momentum = 0

        self.damage_mod = 1

        # Available moves and move weights
        self.moves = [jab, straight, hook, uppercut]
        self.moves_weight = [50, 25, 15, 10]

        self.is_rooked = False
        self.rooked_time = 0

    # ------------------------------------------------------------------
    # Status update / derived stat recalculation
    # ------------------------------------------------------------------
    def update_status(self):
        # recalculate stats based on stamina and damage,
        # stamina weighs more than damage
        stamina_ratio = self.current_stamina / self.max_stamina
        health_ratio = self.current_health / self.max_health

        fatigue_mod = (0.8 * stamina_ratio) + (0.2 * health_ratio)
        power_mod = 0.7 + 0.3 * fatigue_mod

        self.current_accuracy = round(self.max_accuracy * fatigue_mod)
        self.current_strength = round(self.max_strength * power_mod)
        self.current_defense = round(self.max_defense * fatigue_mod)

        # Reload initiative and deplete momentum
        self.max_initiative = round(self.initiative * fatigue_mod)

        self.drift_momentum()
        self.regenerate_stamina()

        self.handle_rooked()
        self.handle_damage_mod()

    # ------------------------------------------------------------------
    # Momentum functions
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Stamina functions
    # ------------------------------------------------------------------
    def regenerate_stamina(self):
        if self.current_stamina < self.max_stamina:
            self.current_stamina += 1

    def decrease_stamina(self, amount):
        if self.current_stamina + amount > 0:
            self.current_stamina -= amount
        else:
            self.current_stamina = 0

    # ------------------------------------------------------------------
    # Initiative functions
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Rooked
    # ------------------------------------------------------------------
    def set_rooked(self):
        self.is_rooked = True
        self.rooked_time = random.randint(1,3)
    
    def handle_rooked(self):
        if self.rooked_time > 0:
            self.is_rooked = True
            self.rooked_time -= 1
        else:
            self.is_rooked = False
        
    def handle_damage_mod(self):
        if self.is_rooked:
            self.damage_mod = 2
        else:
            self.damage_mod = 1
    # ------------------------------------------------------------------
    # Combat state helpers
    # ------------------------------------------------------------------
    def is_knocked_out(self):
        return self.current_health <= 0

    def take_damage(self, amount):
        self.current_health -= amount * self.damage_mod

        self.decrease_stamina(1)
        self.decrease_initiative(4)
        self.decrease_momentum(2)
        
    def determine_hit_severity(self, damage):
        if damage < 0.08 * self.max_health:
            return "light_hit"
        elif damage > 0.08 * self.max_health and damage < 0.18 * self.max_health:
            return "medium_hit"
        elif damage > 0.18 * self.max_health and damage < 0.30 * self.max_health:
            return "hard_hit"
        elif damage > 0.30 * self.max_health:
            return "critical_hit"

        

    # ------------------------------------------------------------------
    # Combat resolution
    # ------------------------------------------------------------------
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
    
    def should_reset(self):
        return self.current_stamina < self.max_stamina * 0.5

    # ------------------------------------------------------------------
    # Debug / display
    # ------------------------------------------------------------------
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Health: {self.current_health} / {self.max_health}\n"
            f"Stamina: {self.current_stamina}\n"
            f"Initative: {self.initiative}\n"
            f"Momentum: {self.momentum}\n"
        )
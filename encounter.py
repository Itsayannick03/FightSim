import random

from fighter import Fighter
from move import Move


class Encounter:
    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        # Fighters participating in this encounter
        self.fighter1 = fighter1
        self.fighter2 = fighter2

        # Active roles, determined by initiative
        self.attacker = None
        self.defender = None

        # Encounter result data
        self.description = None
        self.time_used = 0
        self.move = None
        self.category = None
        self.outcome = None
        self.ends_match = False

    # ------------------------------------------------------------------
    # Initiative resolution
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # Neutral / movement handling
    # ------------------------------------------------------------------
    def handle_neutral(self):
        self.time_used += random.randint(4, 10)

        self.category = "movement"
        self.outcome = "reset"

        self.description = "The fighters circle each other"

    def handle_reset(self):
        self.time_used += random.randint(4, 10)

        self.category = "movement"
        self.outcome = "reset"

        self.description = f"{self.attacker.name} circles around {self.defender.name}"

    # ------------------------------------------------------------------
    # Attack handling
    # ------------------------------------------------------------------
    def handle_hit(self, move: Move):
        damage = self.attacker.calculate_damage(move)
        self.time_used += random.randint(5, 12)

        self.category = "attack"
        self.outcome = "hit"

        self.defender.take_damage(damage)
        hit_severity = self.defender.determine_hit_severity(damage)

        if self.defender.is_knocked_out():
            self.ends_match = True
            self.description = f"{self.attacker.name} knocks {self.defender.name} out with a {move.name}"
        else:
            self.description = f"{self.attacker.name} lands a {move.name} on {self.defender.name}"

    def handle_miss(self, move: Move):
        self.time_used += random.randint(3, 8)

        self.category = "attack"
        self.outcome = "miss"

        self.description = f"{self.attacker.name} misses a {move.name}"

    # ------------------------------------------------------------------
    # Main encounter resolution
    # ------------------------------------------------------------------
    def run(self):
        # Update both fighters before resolving the exchange
        self.fighter1.update_status()
        self.fighter2.update_status()

        # Determine who gets the initiative
        self.resolve_initiative()

        # If neither fighter gets initiative, the exchange stays neutral
        if self.attacker is None or self.defender is None:
            self.handle_neutral()
            return

        # Attacker chooses to reset instead of throwing a strike
        if self.attacker.should_reset():
            self.handle_reset()
            return

        # Otherwise attacker throws a move
        move: Move = self.attacker.get_move()
        self.move = move

        if self.attacker.attack_hits(self.defender, move):
            self.handle_hit(move)
        else:
            self.handle_miss(move)
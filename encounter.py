from fighter import Fighter
from move import Move
import random
jab = Move("jab", 2, 0, 1, 3, 1)
straight = Move("straight", 8, 2, 3, 9, 1)

moves = [jab, straight]

def resolve_initiative(fighter1: Fighter, fighter2: Fighter):
    fighter1_initiative = fighter1.initiative + random.randint(-5, 5)
    fighter2_initiative = fighter2.initiative + random.randint(-5, 5)

    if fighter1_initiative > fighter2_initiative:
        attacker = fighter1
        defender = fighter2
    else:
        attacker = fighter2
        defender = fighter1
    return [attacker, defender]

def subtract_time(time_value, seconds_to_subtract):
    minutes = int(time_value)
    seconds = int(round((time_value - minutes) * 100))

    total_seconds = minutes * 60 + seconds
    total_seconds -= seconds_to_subtract

    if total_seconds < 0:
        total_seconds = 0

    new_minutes = total_seconds // 60
    new_seconds = total_seconds % 60

    return float(f"{new_minutes}.{new_seconds:02}")

def get_time(time_value):
    minutes = int(time_value)
    seconds = int(round((time_value - minutes) * 100))
    return [minutes, seconds]

def encounter(fighter1: Fighter, fighter2: Fighter, time_remaining):
    fighter1.update_status()
    fighter2.update_status()

    attacker, defender = resolve_initiative(fighter1, fighter2)
    move = random.choice(moves)

    if attacker.attack_hits(defender, move):
        damage = attacker.hit(move)
        defender.take_damage(damage)
        print(f"{attacker.name} hit {defender.name} with a {move.name} and dealt {damage} damage")

    else:
        print(f"{attacker.name} tried throwing a {jab.name} but {defender.name} managed to dodge")
    time = random.randint(5, 20)
    time_remaining = subtract_time(time_remaining, time)
    print()
    return time_remaining
    

def round(time_remaining):
    minutes, seconds = get_time(time_remaining)
    print(f"Timer: {minutes}:{seconds}")
    print("---------------")
    




fighter1 = Fighter("Ali", 100, 50, 100, 100, 50, 0)
fighter2 = Fighter("Tyson", 100, 50, 100, 100, 50, 0)

round_nr = 1
time_remaining = 5.0
while not fighter1.is_knocked_out() and not fighter2.is_knocked_out() and time_remaining > 0:
    time_remaining = encounter(fighter1, fighter2, time_remaining)


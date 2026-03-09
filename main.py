from fighter import Fighter
from time import sleep

### Main ###
fighter1 = Fighter("Ali", 100, 65, 10, 45)
fighter2 = Fighter("Tyson", 95, 53, 7, 78)
print("Fight Start!")
print(f"{fighter1.name} vs {fighter2.name}")
print("----------------------------\n")

while(not fighter1.is_knocked_out()  and not fighter2.is_knocked_out() ):
    if(fighter1.punch(fighter2)):
        fighter2.take_damage(fighter1.punch_damage)
        print(f"{fighter1.name} hit {fighter2.name} clean with a punch!")
        print(f"{fighter2.name} took {fighter1.punch_damage} damage!")
    else:
        print(f"{fighter1.name} missed")
    print()
    if(fighter2.punch(fighter1)):
        fighter1.take_damage(fighter2.punch_damage)
        print(f"{fighter2.name} hit {fighter1.name} clean with a punch!")
        print(f"{fighter1.name} took {fighter2.punch_damage} damage!")
    else:
        print(f"{fighter2.name} missed")
    print("----------------------------")
    
if fighter1.is_knocked_out():
    print(f"{fighter1.name} is knocked out!")
else:
    print(f"{fighter1.name} is knocked out!")
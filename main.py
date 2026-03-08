from fighter import Fighter


### Main ###
ali = Fighter("Ali", 100, 65, 10, 45)
tyson = Fighter("Tyson", 95, 53, 7, 78)
print("Fight Start!")
print(f"{ali.name} vs {tyson.name}")
print("----------------------------\n")

while(not ali.is_knocked_out()  and not tyson.is_knocked_out() ):
    print("Ali took 10 damage!")
    ali.take_damage(10)
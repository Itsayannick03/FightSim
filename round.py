from fighter import Fighter
from exchange import Exchange
from time import sleep
class FightRound:
    def __init__(self, fighter1: Fighter, fighter2: Fighter, round_number):
        self.time_remaining = 5 * 60 # 5 minutes

        self.fighter1 = fighter1
        self.fighter2 = fighter2

        self.round_number = round_number

        self.is_over = False
        
    def time_string(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        return f"{minutes}:{seconds:02}"

    def run(self):
        while not self.is_over and self.time_remaining > 0:
            time_left = self.time_string()
            print(f"Round: {self.round_number} {time_left}")
            print("--------------")
            
            
                
            exchange = Exchange(self.fighter1, self.fighter2)
            exchange.run()
            
            self.time_remaining -= exchange.time_used
            if exchange.ends_match:
                self.is_over = True
            print()
            print(self.fighter1)
            print(self.fighter2)
            sleep(1.5)

ali = Fighter("Ali", max_health=100,accuracy=50, strength=100,stamina=100,defense=50,aggression=0)
tyson = Fighter("Tyson", max_health=100,accuracy=50, strength=250,stamina=100,defense=50,aggression=0)

fightRound = FightRound(ali, tyson, 1)
fightRound.run()


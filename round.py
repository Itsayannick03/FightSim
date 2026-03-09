from fighter import Fighter
from exchange import Exchange
class FightRound:
    def __init__(self, fighter1, fighter2, round_number):
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
            print(self.fighter1)
            print(self.fighter2)

ali = Fighter("Ali", 100, 50, 100, 100, 50, 0)
tyson = Fighter("Tyson", 100, 50, 100, 50, 40, 0)  

fightRound = FightRound(ali, tyson, 1)
fightRound.run()


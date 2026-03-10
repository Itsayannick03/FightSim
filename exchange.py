import random
from encounter import Encounter
from fighter import Fighter
class Exchange:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

        self.encounter_count = random.randint(1,3)
  

        self.time_used = 0

        self.ends_match = False
        
        self.encounters = []
    
    def handle_commentary(self):
        commentary = []
        
        first_encounter:Encounter = self.encounters[0]
        sentense = f"{first_encounter.attacker.name}" + f" {first_encounter.description}"
        commentary.append(first_encounter.attacker.name)
        for encounter in self.encounters:
            
        



    def run(self):
        description_parts = []
        for _ in range(self.encounter_count):
            encounter = Encounter(self.fighter1, self.fighter2)
            encounter.run()
            self.encounters.append(encounter)

            self.time_used += encounter.time_used

            if encounter.ends_match:
                self.ends_match = True
                description_parts.append(encounter.description)
                break

            description_parts.append(encounter.description)
        description = ", ".join(description_parts)
        print(description)


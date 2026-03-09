import random
from encounter import Encounter
from fighter import Fighter
class Exchange:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

        self.encounter_count = random.randint(1,4)
  

        self.time_used = 0

        self.ends_match = False

    # def classify_transition(enc1, enc2):

    #     same_attacker = enc1.attacker == enc2.attacker

    #     if same_attacker:

    #         if enc1.outcome == "hit" and enc2.outcome == "hit":
    #             return "combo"

    #         if enc1.outcome == "hit" and enc2.outcome == "miss":
    #             return "follow_up"

    #         if enc1.outcome == "miss" and enc2.outcome == "hit":
    #             return "recovered_attack"

    #         if enc1.outcome == "miss" and enc2.outcome == "miss":
    #             return "failed_pressure"

    #     else:

    #         if enc1.outcome == "miss" and enc2.outcome == "hit":
    #             return "counter"

    #         if enc1.outcome == "hit" and enc2.outcome == "hit":
    #             return "retaliation"

    #         if enc1.outcome == "hit" and enc2.outcome == "miss":
    #             return "defended"

    #     return "neutral"
    
    # def get_conjuncture(self, encounter1: Encounter, encounter2: Encounter):
    #     CONNECTOR_TABLE = {

    #         "combo": [
    #             "then",
    #             "and follows up with",
    #             "and continues with",
    #             "before firing"
    #         ],

    #         "follow_up": [
    #             "but the follow-up",
    #             "before missing with",
    #             "and tries another"
    #         ],

    #         "recovered_attack": [
    #             "but then lands",
    #             "before finding the mark with",
    #             "and connects with"
    #         ],

    #         "failed_pressure": [
    #             "and",
    #             "but also misses with"
    #         ],

    #         "counter": [
    #             "but",
    #             "only for",
    #             "and"
    #         ],

    #         "retaliation": [
    #             "but",
    #             "and"
    #         ],

    #         "neutral": [
    #             "then",
    #             "moments later",
    #             "shortly after"
    #         ]
    #     }
        
    #     transition = self.classify_transition(encounter1, encounter2)
    #     return random.choice(CONNECTOR_TABLE[transition])
    
    # def build_description(self):
    #     if self.encounter_count == 1:
    #         encounter = self.encounters[0]

    #     else:
    #         description_parts = []
    #         for first_encounter, second_encounter in zip(self.encounters, self.encounters[1:]):
    #             conjuncture = self.get_conjuncture(first_encounter, second_encounter)

        # else:
        #     


        #     for current_encounter, next_encounter in zip(self.encounters, self.encounters[1:]):
        #         first_attacker = current_encounter.attacker
        #         second_attacker = next_encounter.attacker

        #         if first_attacker == second_attacker:
        #             if current_encounter.outcome == "hit" and next_encounter.outcome == "hit":
        #                 conjuncture = random.choice([
        #                     "then",
        #                     "and follows up with",
        #                     "and quickly follows with",
        #                     "before throwing",
        #                     "and immediately throws",
        #                     "and continues with"
        #                 ])

        

    def run(self):
        description_parts = []
        for _ in range(self.encounter_count):
            encounter = Encounter(self.fighter1, self.fighter2)
            encounter.run()

            self.time_used += encounter.time_used

            if encounter.ends_match:
                self.ends_match = True
                description_parts.append(encounter.description)
                break

            description_parts.append(encounter.description)
        description = ", ".join(description_parts)
        print(description)


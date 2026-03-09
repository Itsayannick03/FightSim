class Move:
    def __init__(self, name, base_damage, accuracy_mod, stamina_cost_hit, stamina_cost_miss, time_to_perform, category):
        self.name = name
        self.base_damage = base_damage
        self.stamina_cost_hit = stamina_cost_hit
        self.stamina_cost_miss = stamina_cost_miss
        self.accuracy_mod = accuracy_mod
        self.time_to_perform = time_to_perform
        self.category = category



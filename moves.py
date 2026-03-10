from move import Move

jab = Move(name="jab", base_damage=2, accuracy_mod= 0, stamina_cost_hit=1, stamina_cost_miss=3, time_to_perform=1, category="strike")
straight = Move("straight", 8, 2, 3, 9, 1, "strike")
hook = Move("hook", 10, -1, 4, 10, 2, "strike")
uppercut = Move("uppercut", 14, -2, 6, 12, 3, "strike")
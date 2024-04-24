class Monster:
    health = 40

    def __init__(self, damage, attack_speed):
        self.damage = damage
        self.attack_speed = attack_speed
    
    def damage_per_second(self):
        dps = self.damage / self.attack_speed
        print(dps)

Kyle = Monster(100, 2)
print(Kyle)
print(Kyle.health)
Kyle.damage_per_second()
Monster.damage_per_second()
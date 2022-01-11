import random
import races
import skill_tree
import buff

class entity:
    def __init__(self, level):
        self.level = level
        if self.level > 120:
            self.level = 120
        
        level_multiplier = 25
        if 60 > self.level >= 30:
            level_multiplier = 50
        elif 90 > self.level >= 60:
            level_multiplier = 75
        elif self.level >= 90:
            level_multiplier = 100

        health_multiplier = 10
        if 20 > self.level >= 10:
            health_multiplier = 20
        elif 30 > self.level >= 20:
            health_multiplier = 50
        elif 50 > self.level >= 30:
            health_multiplier = 75
        elif 100 > self.level >= 50:
            health_multiplier = 100
        elif self.level >= 100:
            health_multiplier = 120
        
        self.skills = []
        self.race = random.choice(races.l_rc)
        if self.race == 'Slime':
            skill_tree.gf.append('Mimic')
        
        rc_buff = buff.rcb[self.race]
        self.hp = int(random.randint(50, 125) + ((health_multiplier * self.level) * rc_buff))
        arc_buff = buff.arcb[self.race]
        self.arcanium = int(100 + ((self.level * level_multiplier) * arc_buff))
        self.strength = random.randint(5, 50)
        if self.strength >= 40:
            self.skills.append('Berserker')
        
        self.intelligence = random.randint(0, 100)
        if self.intelligence >= 85:
            self.skills.append('Analize')
        
        self.gift_1 = random.choice(skill_tree.gf)
        self.gift_2 = random.choice(skill_tree.gf)
        if self.gift_1 == self.gift_2:
            self.final_gift = 'Great ' + self.gift_1
        else:
            self.final_gift = self.gift_1 + ' & ' + self.gift_2
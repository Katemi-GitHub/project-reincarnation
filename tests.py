import random
import races
import skill_tree
import buff
import json

# Prototype 1
class Gen_Entity:
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
        self.arkanius = int(100 + ((self.level * level_multiplier) * arc_buff))
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
        self.state = 'alive'
    
    def attack(self, enemy_hp):
        enemy_hp -= self.strength
        return enemy_hp
    
    def get_damaged(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.state = 'defeat'

    def stats(self):
        print(f'    HP: {self.hp}\n    Race: {self.race}\n    Gift: {self.final_gift}\n    Skills: {self.skills}\n    Level: {self.level}\n    Arkanius: {self.arkanius}\n')

entity = Gen_Entity(random.randint(2*2, 12/2))
#entity.stats()

running = True
entity_data = {}

while running:

    command = input().split(' ')
    if command[0] == 'give':
        if command[1] == 'skill':
            valid_skill = False
            error = False
            if len(command) == 4:
                skill_tuple = (command[2], command[3])
                command[2] = ' '.join(skill_tuple)
            #-----------------------------------------------------------------
            for i in range(len(skill_tree.skill)):
                if command[2] == skill_tree.skill[i]:
                    valid_skill = True
                else:
                    error = True
            if valid_skill == True:
                if not entity.skills.count(command[2]) >= 1:
                    entity.skills.append(command[2])
                    entity.stats()
                else:
                    print('Error: This skill is already activated!\n')
            elif error == True:
                print('Error: No skill found!\n')
            #-----------------------------------------------------------------

    if command [0] == 'remove':
        if command[1] == 'skill':
            valid_skill = False
            error = False
            if len(command) == 4:
                skill_tuple = (command[2], command[3])
                command[2] = ' '.join(skill_tuple)
            for i in range(len(entity.skills)):
                if command[2] == entity.skills[i]:
                    valid_skill = True
                else:
                    error = True
            if valid_skill == True:
                entity.skills.remove(command[2])
                entity.stats()
            elif error == True:
                print('Error: This skill is not activated!\n')
            elif len(entity.skills) == 0:
                print('Error: There are no skills left!\n')

    if command[0] == 'save':
        entity_name = command[1]
        entity_data[entity_name] = {
            'Race' : entity.race,
            'Level' : entity.level,
            'HP' : entity.hp,
            'Arkanius' : entity.arkanius,
            'Intelligence' : entity.intelligence,
            'Strength' : entity.strength,
            'Gifts' : entity.final_gift,
            'Skills' : entity.skills
        }

        with open('entity_data/entity_data.txt', 'w') as outfile:
            json.dump(entity_data, outfile, indent=4, separators=(',', ':'))

    if command[0] == 'regen':
        print('New Entity:')
        entity = Gen_Entity(random.randint(4, 6))
        entity.stats()
            
    if command[0] == 'close':
        running = False
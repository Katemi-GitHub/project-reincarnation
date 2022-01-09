import random
import races
import skill_tree
import buff

# Prototype 1
class Player:
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
        
        self.abilities = []
        self.race = random.choice(races.l_rc)
        if self.race == 'Slime':
            skill_tree.gf.append('Mimic')
        
        rc_buff = buff.rcb[self.race]
        self.hp = int(random.randint(50, 125) + ((health_multiplier * self.level) * rc_buff))
        arc_buff = buff.arcb[self.race]
        self.arcanium = int(100 + ((self.level * level_multiplier) * arc_buff))
        self.strength = random.randint(5, 50)
        if self.strength >= 40:
            self.abilities.append(skill_tree.hab[11])
        
        self.intelligence = random.randint(0, 100)
        if self.intelligence >= 85:
            self.abilities.append(skill_tree.hab[0])
        
        self.gift_1 = random.choice(skill_tree.gf)
        self.gift_2 = random.choice(skill_tree.gf)
        if self.gift_1 == self.gift_2:
            self.final_gift = 'Extra ' + self.gift_1
        else:
            self.final_gift = self.gift_1 + ' & ' + self.gift_2

    def stats(self):
        print(f'HP: {self.hp}\nRace: {self.race}\nGift: {self.final_gift}\nSkills: {self.abilities}\nLevel: {self.level}\nArcanium: {self.arcanium}\n')

player = Player(120)
player.stats()

running = True

while running:

    command = input().split(' ')
    if command[0] == 'give':
        if command[1] == 'ability':
            valid_ability = False
            error = False
            if len(command) >= 4:
                ability_tuple = (command[2], command[3])
                command[2] = ' '.join(ability_tuple)
            for i in range(len(skill_tree.hab)):
                if command[2] == skill_tree.hab[i]:
                    valid_ability = True
                else:
                    error = True
            if valid_ability == True:
                if not player.abilities.count(command[2]) >= 1:
                    player.abilities.append(command[2])
                    player.stats()
                else:
                    print('Error: This ability is already actived!')
            elif error == True:
                print('Error: No ability found!')

    elif command[0] == 'remove':
        if command[1] == 'ability':
            if len(command) >= 4:
                ability_tuple = (command[2], command[3])
                command[2] = ' '.join(ability_tuple)
            player.abilities.remove(command[2])
            player.stats()

    elif command[0] == 'evolve':
        None
    
    elif command[0] == 'close':
        running = False
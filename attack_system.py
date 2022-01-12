import gen_entities
import random

player = gen_entities.Gen_Entity(random.randint(4, 6))
enemy = gen_entities.Gen_Entity(random.randint(4, 6))

player.stats()

print('Player Strength: ' + str(player.strength))
print('Enemy HP: ' + str(enemy.hp))

enemy.get_damaged(player.strength)
print(enemy.hp)
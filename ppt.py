import random

print('Elije piedra, papel o tijeras')
p_choice = input()
c_choice = random.choice([1, 2, 3])

if p_choice == 'piedra':
    p_choice = 1
elif p_choice == 'papel':
    p_choice = 2
elif p_choice == ('tijeras' or 'tijera'):
    p_choice = 3

if c_choice == 1:
    print('piedra')
elif c_choice == 2:
    print('papel')
elif c_choice == 2:
    print('tijera')

if p_choice == 1 and c_choice == 3:
    print('\nTu win! muchas congratuleishons')
elif p_choice == 2 and c_choice == 1:
    print('\nTu win! muchas congratuleishons')
elif p_choice == 3 and c_choice == 2:
    print('\nTu win! muchas congratuleishons')
else:
    print('\nTu lose! noob ggez')
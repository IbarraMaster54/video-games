from random import randint 
import os
def dices():
    d1 = randint(1,6)
    d2 = randint(1,6)
    print(f'Dado uno {d1}\nDado dos:{d2}')
    if(d2==d1):
        print('Los dados son iguales')
    else:
        print('Los dados no son iguales')

os.system('clear')
dices()
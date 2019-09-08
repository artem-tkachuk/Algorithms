# The simulation of Monty Hall problem

from random import random

n =  1000000
cars = 0
goats = 0
doors = [0, 0, 0]

for i in range(n):
    doors[0] = int(random() * 100 % 2)
    if doors[0] == 1:
        doors[1], doors[2] = 0, 0
    else:
        doors[1] = int(random() * 100 % 2)
        doors[2] = 1  if  doors[1] == 0 else 0
    choice = int(random() * 100 % 3)    #choose random door
    if doors[choice] == 1:
        cars += 1
    else:
        goats += 1

print(f'Simulated {n} times:\n'
      f'If you never switch the door (stay on your first choice),\n'
      f'the probability of winning is {float(cars) * 100 / n}% and '
      f'losing is {float(goats) * 100 / n}%')

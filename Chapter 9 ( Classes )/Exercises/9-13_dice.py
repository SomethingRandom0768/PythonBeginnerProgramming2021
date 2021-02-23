import random

class Die:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        randomNumber = random.randint(1, 6)
        print(randomNumber, end=' ')

firstDice = Die()

for i in range(0, 11):
    firstDice.roll_die()

print("")

secondDice = Die(10)

for i in range(0, 11):
    secondDice.roll_die()

print("")

thirdDice = Die(20)

for i in range(0, 11):
    thirdDice.roll_die()
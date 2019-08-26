import random

class Dice:

    def __init__(self):
        self.numbers = [1,2,3,4,5,6]
    
    def spin_dice(self):
        number = random.choice(self.numbers)
        return number
        
from dice import Dice

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0 #stores position on board

    def move_position(self):
        spinner = Dice()
        number = spinner.spin_dice()
        print(f"{self.name}'s spin was {number}")
        self.position = self.position + number
        print(f"{self.name}'s new position is {self.position}")

        
    
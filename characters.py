from random import randint
class player:
    magic_dice = 8
    bow_dice = 10
    sword_dice = 8
    max_life_points = 12

    def __init__(self, name):
        self.name = name
        self.current_life = self.max_life_points

    def roll_dices(self):
        dices = [["magic", randint(1, self.magic_dice)], ["bow", randint(1, self.bow_dice)],
                 ["sword", randint(1, self.sword_dice)]]
        return dices

    def attack(self):
        dices = self.roll_dices()
        dices = sorted(dices, key=lambda x: x[1], reverse=True)
        return dices[0]

    def defend(self,weapon,dmgs):
        defend = dict(self.roll_dices())
        defend = defend[weapon]
        if defend < dmgs :
            self.current_life -= (dmgs - defend)
        return defend

class Warrior(player):
    magic_dice = 8
    bow_dice = 10
    sword_dice = 12
    max_life_points = 16

class Archer(player):
    magic_dice = 10
    bow_dice = 12
    sword_dice = 8
    max_life_points = 12

class Wizard(player):
    magic_dice = 12
    bow_dice = 10
    sword_dice = 8
    max_life_points = 12







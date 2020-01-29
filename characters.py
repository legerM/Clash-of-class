from random import randint


class Player:
    magic_dice = 8
    bow_dice = 10
    sword_dice = 8
    max_life_points = 12

    def __init__(self, name):
        self.name = name
        self.current_life = self.max_life_points
        self._height = randint(170, 190)
        self._weight = randint(70, 90)

    def __repr__(self):
        return self.name + " the " +self.__class__.__name__

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

    def get_height(self):
        return self._height

    def set_height(self,value):

        self._height = value

    height = property(get_height, set_height)

    def get_weight(self):
        return self._weight

    def set_weight(self, value):
        self._weight = value

    weight = property(get_weight,set_weight)


class Warrior(Player):
    sword_dice = 12
    max_life_points = 16

    def attack(self):
        bonus=0
        weapon, dmgs = super().attack()
        if weapon is "magic":
            bonus += self.weight // 30
            dmgs += bonus
        if weapon is "bow":
            bonus += (self.height-170) % 3
            dmgs += bonus

        return {"weapon": weapon, "bonus": bonus, "dmgs": dmgs}
    # def __repr__(self):
    #     return self.name + " the " + Warrior.__name__


class Archer(Player):
    magic_dice = 10
    bow_dice = 12

    # def __repr__(self):
    #     return self.name + " the " + Archer.__name__

    def attack(self):
        weapon, dmgs = super().attack()
        bonus = 1
        if weapon in ["sword", "magic"]:
            dmgs += bonus
            if weapon is "sword":
                bonus += self.height // 40
                dmgs += bonus
            if weapon is "magic":
                bonus += self.weight // 20
                dmgs += bonus
        return {"weapon": weapon, "bonus": bonus, "dmgs": dmgs}


class Wizard(Player):
    magic_dice = 12

    def attack(self):
        bonus = 0
        weapon, dmgs = super().attack()
        roll_magic_twice = dict(self.roll_dices())["magic"]
        if roll_magic_twice > dmgs:
            return {"weapon" : "magic", "dmgs" : roll_magic_twice , "bonus": bonus}
        if weapon is "sword" :
            bonus += (self.weight+self.height) // 40
            dmgs += bonus
        if weapon is "bow":
            bonus += (self.height-170) % 3
            dmgs += bonus
        return {"weapon": weapon, "bonus": bonus, "dmgs": dmgs}
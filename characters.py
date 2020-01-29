from random import randint


class Player:
    magic_dice = 8
    bow_dice = 10
    sword_dice = 8
    max_life_points = 12
    sword_bonus = 0
    bow_bonus = 0

    def __init__(self, name):
        self.name = name
        self._current_life = self.max_life_points
        self._height = randint(170, 190)
        self._weight = randint(70, 90)


    def __repr__(self):
        return self.name + " the " + self.__class__.__name__

    def roll_dices(self):
        dices = [["magic", randint(1, self.magic_dice)], ["bow", randint(1, self.bow_dice)],
                 ["sword", randint(1, self.sword_dice)]]
        return dices

    def attack(self):
        dices = self.roll_dices()
        dices = sorted(dices, key=lambda x: x[1], reverse=True)
        weapon,dmgs =dices[0]
        if weapon == "sword":
            dmgs += self.sword_bonus
        if weapon == "bow":
            dmgs += self.bow_bonus
        return weapon, dmgs

    def defend(self,weapon, dmgs):
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

    def get_currentlife(self):
        return self._current_life

    def set_currentlife(self,value):
        if value <= 0 :
            self._current_life = 0
        else:
            self._current_life = value

    current_life=property(get_currentlife,set_currentlife)



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


class Archer(Player):
    magic_dice = 10
    bow_dice = 12

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


class Dwarf:
    sword_bonus = 2


class Elf:
    bow_bonus = 2


class ElfWizard(Elf, Wizard):
    pass


class ElfWarrior(Elf, Warrior):
    pass


class ElfArcher(Elf, Archer):
    pass


class DwarfWizard(Dwarf,Wizard):
    pass


class DwarfWarrior(Dwarf,Warrior):
    pass


class DwarfArcher(Dwarf,Archer):
    pass
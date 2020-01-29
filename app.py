import characters
import random

def main():
    merlin = characters.Wizard("Merlin")
    rolanculer = characters.Warrior("Rolanculé")
    gnuette = characters.Archer("gnuette")
    character = [merlin,rolanculer,gnuette]
    attacker = random.choice(character)
    defender = random.choice(character)
    while attacker == defender :
        defender = random.choice(character)

    atk = attacker.attack()
    # weapon =atk["weapon"]
    # dmgs=atk["dmgs"]
    # bonus=atk["bonus"]
    print(str(attacker) + " use " + atk["weapon"] + " and make "+str(atk["dmgs"])+" dmgs whose " + str(atk["bonus"])+ " attack bonus " )
    print(str(defender) + " defend with "+atk["weapon"]+ " and block " + str(defender.defend(atk["weapon"],atk["dmgs"]))+" dmgs")
    print(str(defender) + " has "+ str(defender.current_life)+" HP")
    print(str(attacker) + " has " + str(attacker.current_life)+" HP")


if __name__ == "__main__":
    main()

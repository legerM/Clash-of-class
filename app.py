import characters
import random


def main():
    merlin = characters.ElfWizard("Merlin")
    gnu = characters.DwarfWarrior("Gnu")
    gnuette = characters.ElfArcher("gnuette")
    character = [merlin, gnu, gnuette]
    attacker = random.choice(character)
    defender = random.choice(character)
    while attacker == defender:
        defender = random.choice(character)

    atk = attacker.attack()

    print(str(attacker) + " use " + atk["weapon"] + " and make "+str(atk["dmgs"])+" dmgs whose " + str(atk["bonus"])+ " attack bonus " )
    print(str(defender) + " defend with " +atk["weapon"] + " and block " + str(defender.defend(atk["weapon"], atk["dmgs"])) + " dmgs")
    print(str(defender) + " has "+ str(defender.current_life)+" HP")
    print(str(attacker) + " has " + str(attacker.current_life)+" HP")


if __name__ == "__main__":
    main()

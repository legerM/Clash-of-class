import characters

merlin = characters.Wizard("Merlin")
rolanculer = characters.Warrior("Rolanculé")
gnuette = characters.Archer("gnuette")
weapon, dmgs = merlin.attack()
print(merlin.name +" use "+ weapon + " and make "+str(dmgs)+" dmgs")
print(rolanculer.name+ " defend with "+weapon+ " and block " + str(rolanculer.defend(weapon,dmgs))+" dmgs")
print(rolanculer.name + " has "+ str(rolanculer.current_life)+" HP")
print(merlin.name+ " has " + str(merlin.current_life)+" HP")

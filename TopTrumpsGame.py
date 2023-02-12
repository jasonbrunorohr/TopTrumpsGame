#Top Trumps game Portfolio Project Codecademy CS

#dictionary of Star Wars Spaceships

spaceships = []

#function to add new cards to the dictionary spaceships

def new_card(name, size, speed, firepower, agility, power):
    card_dictionary = {"name": name, "size": size, "speed": speed, "firepower": firepower, "agility": agility, "power": power}
    spaceships.append(card_dictionary)
    

#playing cards deck
new_card("Slave1", 4, 93, 7, 17, 2)
new_card("Republican Gunship", 5, 58, 8, 13, 2)
new_card("Millenum Falcon", 6, 100, 7, 20, 3)
new_card("AT-AT", 6, 64, 8, 8, 2)
new_card("X-Wing Fighter", 5, 80, 6, 18, 3)
new_card("Jedi Star Fighter", 4, 70, 6, 16, 1)
new_card("AT-ST", 4, 69, 5, 11, 2)
new_card("Star Destroyer", 8, 90, 9, 5, 3)
new_card("Podracer", 2, 70, 0, 19, 1)



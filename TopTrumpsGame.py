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
new_card("Solar Sailor", 20, 98, 12, 16, 1)


#classes of players 
player_name = input("To start this battle of Star Wars Top Trumps, please let me know your name: ")
enemy_name = input("What would you like the name of your opponent to be: ")
class Player():

    def __init__(self, name):
        self.name = name 
        self.cards = []
        self.wins = 0 
        print("Hi " + self.name + ". Good Luck!")
    
    def __repr__(self):
        return self.name + ", you have " + str(self.wins) + " wins!"

#instances of players 
npc = Player(enemy_name)
main_player = Player(player_name)
print("Give me some time to shuffle your cards quickly...")
print("...")
print("...")
import random 



#function to shuffle the cards and give them to each player:

def shuffled_deck(unshuffled_deck, mainplayer, npc):
    shuffled_indices = list(range(len(unshuffled_deck)))
    random.shuffle(shuffled_indices)
    random.shuffle(shuffled_indices)
    split_index = len(shuffled_indices) // 2
    deck1_indices = shuffled_indices[:split_index]
    deck2_indices = shuffled_indices[split_index:]
    deck1 = [unshuffled_deck[i] for i in deck1_indices]
    deck2 = [unshuffled_deck[i] for i in deck2_indices]
    mainplayer.cards = deck1
    npc.cards = deck2
    print("Here's the deck for you " + mainplayer.name + " and here is yours " + npc.name + ".")
    return (deck1, deck2)

shuffled_deck(spaceships, main_player, npc)    

    
        




#Top Trumps game Portfolio Project Codecademy CS
import random
#dictionary of Star Wars Spaceships

spaceships = []

#function to add new cards to the dictionary spaceships

def new_card(name, size, speed, firepower, agility, power):
    card_dictionary = {"name": name, "size": size, "speed": speed, "firepower": firepower, "agility": agility, "power": power}
    spaceships.append(card_dictionary)
    

#playing cards deck
new_card("Slave1", 4, 93, 7, 17, 1)
new_card("Republican Gunship", 5, 58, 8, 13, 2)
new_card("Millenum Falcon", 7, 100, 5, 20, 3)
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
        self.won_last = None
        
    
    def __repr__(self):
        return self.name + ", you have " + str(self.wins) + " wins!"

    #method to choose a stat and have card either be given to the other player or being received from the loser
    
    def play(self, other_player):
        print("You're card is " + self.cards[0]["name"] + ". It's stats are following: size " + str(self.cards[0]["size"]) + "   speed " + str(self.cards[0]["speed"]) + "   firepower " + str(self.cards[0]["firepower"]) + "   agility " + str(self.cards[0]["agility"]) + "   power " + str(self.cards[0]["power"]))
        if self.won_last is None:
            print(self.name + " starts the game.")
            stat = input(self.name + " choose a stat you want to trump with: ")
            if stat not in self.cards[1].keys():
                stat = input("I think you misspelled that. Go again: ")
            self.won_last = False
            other_player.won_last = False
        elif self.won_last:
            stat = input(self.name + " choose a stat you want to trump with: ")
        else:
            print(other_player.name + " won the last round.")
            keys = [key for key in other_player.cards[0].keys() if key != "name"]
            stat = random.choice(keys)
            print(other_player.name + " chooses " + stat)
                
    
        self_card_stat = self.cards[0][stat]
        other_card_stat = other_player.cards[0][stat]
        
        if self_card_stat > other_card_stat:
            print(f"{self.name} wins this round!")
            self.cards.append(other_player.cards.pop(0))
            self.cards.append(self.cards.pop(0))
            self.won_last = True
            other_player.won_last = False
        elif self_card_stat < other_card_stat:
            print(f"{other_player.name} wins this round!")
            other_player.cards.append(self.cards.pop(0))
            other_player.cards.append(other_player.cards.pop(0))
            self.won_last = False
            other_player.won_last = True
        else:
            print("It's a tie, you've got to choose again...")
            self.play(other_player)
            
        print(f"{self.name} has {str(len(self.cards))} cards, while {other_player.name} has {str(len(other_player.cards))}.")


#instances of players 
npc = Player(enemy_name)
main_player = Player(player_name)
print("Give me some time to shuffle your cards quickly...")
print("...")
print("...")




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



#function to loop to keep playing until one of the players has all the cards
def gameplay(main_player, npc):

    while len(main_player.cards) > 0 and len(npc.cards) >0:
            main_player.play(npc)

    if len(main_player.cards) == 0:
        print(npc.name + " wins the game!!!")
        npc.wins += 1

    elif len(npc.cards) == 0:
        print(main_player.name + " wins the game!!!")
        main_player.wins += 1
    
    print(f"{main_player.name} has {str(main_player.wins)} wins, while {npc.name} has won {str(npc.wins)} games.")

    play_again = input("Do you want to play a new game? Enter yes or no: ")

    if play_again == "yes":
        gameplay(main_player, npc)
    else: 
        print("See you soon then you sore loser ;)")

gameplay(main_player, npc)





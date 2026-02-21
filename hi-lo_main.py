import random
import time

class LifeSystem:
    def wrong_guess(self):
        pass
    def game_over(self):
        pass
    def status(self):
        return ""
class NormalMode(LifeSystem):
    def __init__(self):
        self.lives = 10
    def status(self):
        return f"lives: {self.lives}"
    def wrong_guess(self):
        self.lives -= 1
        return "lives: -1"
    def game_over(self):
        return self.lives <= 0
class RussianRoulette(LifeSystem):
    def __init__(self):
        self.chamber = 1
        self.bullet = random.randint(1,6)
        self.dead = False
    def wrong_guess(self):
        print("Pulling the trigger...")
        time.sleep(1)
        if self.chamber == self.bullet:
            self.dead = True
            return "*BANG!*"
        else:
            self.chamber += 1
            return "*click*"
    def game_over(self):
        return self.dead
    
cards = [
    "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", 
    "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", 
    "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", 
    "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"  
]
card_values = {
   "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13
}
all_spades = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"]
all_hearts = ["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"]
all_clubs = ["A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]
all_diamonds = ["A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦"]
score = 0

def display_cards(suit_name, suit_cards):
    print(f"{suit_name}", end="")
    for card in suit_cards:
        if card in cards:
            print(card, end=" ")
        else:
            if card in ["10♠", "10♥", "10♣", "10♦"]:
                print("xx", end="  ")
            else:
                print("xx", end=" ")
    print()

while True:
    mode = input("Select the difficulty\n1. Normal mode\n2. Luckmaxxing\n")
    if mode == '1':
        life_system = NormalMode()
        break
    elif mode == '2':
        life_system = RussianRoulette()
        print("Good luck!")
        time.sleep(0.5)
        break
    else:
        print("Invalid input!")

current_card = random.choice(cards)
cards.remove(current_card)
print("=" * 50)
print(f"Welcome to the Hi-Lo game!\nRules:\nCards are odrered form lowest to highest\nType 'higher' if the next card is higher.\nType 'lower' if the card is lower.\nType 'quit' to quit the game.")
time.sleep(1)

while True:
    if not cards:
        print("\nNo more cards!\nCongratulations! You beat the game!")
        break
    print("\n===Cards Remaining===")    
    display_cards("Spades:   ", all_spades)
    display_cards("Hearts:   ", all_hearts)
    display_cards("Clubs:    ", all_clubs)
    display_cards("Diamonds: ", all_diamonds)
    print(f"\nCard picked: {current_card}")
    status = life_system.status()
    if status:
        print(status)
    guess = input(f"Will the next card be Higher or Lower?\n(Tip: Just type 'h' or 'l' if you're lazy.)\n").lower().strip()
    #More inputs
    if guess == "quit":
        print("\nThank you for playing!")
        break
    if guess not in ["higher","lower","h","l"]:
        print("Invalid input!")
        continue
    #Game logic
    next_card = random.choice(cards)
    cards.remove(next_card)
    current_value = card_values[current_card[:-1]]
    next_value = card_values[next_card[:-1]]
    if (guess == "higher" or guess == "h") and next_value >= current_value:
        score += 1
        print("Correct!")
        time.sleep(0.5)
    elif (guess == "lower" or guess == "l") and next_value <= current_value:
        score += 1
        print("Correct!")
        time.sleep(0.5)
    else:
        print("Wrong!")
        time.sleep(0.5)
        message = life_system.wrong_guess() 
        print(message)
        time.sleep(1) 
        if life_system.game_over():
            print("Game over!")
            break
    current_card = next_card
print(f"Final Score: {score}")

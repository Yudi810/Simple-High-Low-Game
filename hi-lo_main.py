import random
import time
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
lives = 10
current_card = random.choice(cards)
cards.remove(current_card)
print("==================================================")
print(f"Welcome to the Hi-Lo game!\nRules:\nCards are odrered form lowest to highsest\nType 'higher' if the next card is higher.\nType 'lower' if the card is lower.\nType 'quit' to quit the game.")
time.sleep(1)

while True:
    if not cards:
        print("\nNo more cards!\nCongratulations! You beat the game!")
        break
    print("\n===Cards Remaining===")
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
    display_cards("Spades:   ", all_spades)
    display_cards("Hearts:   ", all_hearts)
    display_cards("Clubs:    ", all_clubs)
    display_cards("Diamonds: ", all_diamonds)
    print(f"\nCard picked: {current_card}")
    guess = input(f"Will the next card be Higher or Lower?\n(Tip: Just type 'h' or 'l' if you're lazy.)\n(Current lives: {lives})\n").lower().strip()
    #More inputs
    if not guess:
        print("Please enter something!")
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
    elif (guess == "lower" or guess == "l") and next_value <= current_value:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        lives -= 1
        if lives <= 0:
            time.sleep(1)
            print("You're out of lives! Game over!")
            break
    time.sleep(0.5) 
    current_card = next_card
print(f"Final Score: {score}")

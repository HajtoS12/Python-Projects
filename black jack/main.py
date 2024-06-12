
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
player_deck = []
computer_deck = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == "y":
    run = True

while run:
    for a in range (0,2):
        player_deck += random.choices(cards)
        computer_deck += random.choices(cards) 
    print(f" Your cards: {player_deck}, current score: {sum(player_deck)}\n Computer's first card: {computer_deck[0]}")
    
    next = True
    while sum(player_deck) <=21 and next == True:
        next_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_card == "y":
            player_deck += random.choices(cards)
            if player_deck[len(player_deck)-1] == 11 and sum(player_deck) > 21:
                player_deck[len(player_deck)-1] = 1
            print(f" Your cards: {player_deck}, current score: {sum(player_deck)}") 
        else:
            next= False


    print(f"Your final hand: {player_deck}, final score: {sum(player_deck)}")
    while sum(computer_deck) <17:
        computer_deck += random.choices(cards)
        if computer_deck[len(computer_deck)-1] == 11 and sum(computer_deck) > 21:
            computer_deck[len(computer_deck)-1] = 1

    print(f"Computer's final hand: {computer_deck}, final score: {sum(computer_deck)}")
    user_score = sum(player_deck)
    computer_score = sum(computer_deck)

    if user_score == computer_score:
        print("Draw 🙃")
    elif computer_score == 21:
        print("Lose, opponent has Blackjack 😱")
    elif user_score == 21:
        print("Win with a Blackjack 😎")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")


    run = False


  


    

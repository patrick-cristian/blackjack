import random
from os import system

possible_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'ace', 'queen', 'king', 'jack']
special_cards = ['ace', 'queen', 'king', 'jack']
valid_inputs = ['y', 'n']

special_cards_converter = {
    'ace': 11,
    'queen': 10,
    'king': 10,
    'jack': 10,
}

def add_current_score(current_card):

    if current_card in special_cards:
        return special_cards_converter[current_card]
    else:
        return current_card

def clear():
    system('cls')


end_of_game = False

while not end_of_game:

    clear()
    end_of_current_round = False
    bust = False
    blackjack = False
    ace_transformation = True
    player_cards = [random.choice(possible_cards), random.choice(possible_cards)]
    player_score = add_current_score(player_cards[0]) + add_current_score(player_cards[1])
    computer_cards = [random.choice(possible_cards)]
    computer_score = add_current_score(computer_cards[0])

    if player_score > 21 and "ace" in player_cards:
        player_score -= 10
    elif player_score == 21:
        blackjack = True
    
    print(f"Your cards: {player_cards}.\nYour score: {player_score}.")
    print(f"Computer's card: {computer_cards}")

    while not end_of_current_round and not bust and not blackjack:

        should_continue_round = input("Do you wish to draw another card? Type 'y' to draw or 'n' to end the round.\n").lower() 
        while should_continue_round not in valid_inputs:
            print("Invalid input.")
            should_continue_round = input().lower()
        
        if should_continue_round == 'y':
            new_card_player = random.choice(possible_cards)
            player_cards.append(new_card_player)
            if player_cards.count('ace') > 1 and new_card_player == 'ace':
                player_score += 1
            else:
                player_score += add_current_score(new_card_player)
            
            if player_score > 21 and "ace" in player_cards and ace_transformation:
                player_score -= 10
                ace_transformation = False
            
            if player_score > 21:
                bust = True

            clear()
            print(f"Your cards: {player_cards}.\nYour score: {player_score}.")
            print(f"Computer's card: {computer_cards}")

            
        else:
            end_of_current_round = True
    
    ace_transformation = True
    while computer_score < 17 and not bust and not blackjack:

        new_card_computer = random.choice(possible_cards)
        computer_cards.append(new_card_computer)
        if computer_cards.count('ace') > 1 and new_card_computer == 'ace':
            computer_score += 1
        else:
            computer_score += add_current_score(new_card_computer)
        
        if computer_score > 21 and "ace" in computer_cards and ace_transformation:
                computer_score -= 10
                ace_transformation = False
        
    
    print(f"Final dealer cards: {computer_cards}")
    
    if bust:
        print(f"You went over ({player_score}). You lost.")
    elif computer_score > 21:
        print(f"Dealer went over ({computer_score}). You won.")
    elif player_score == computer_score:
        print("It's a draw. No one wins.")
    elif blackjack:
        print("Blackjack! You won.")
    elif computer_score == 21 and len(computer_cards) == 2:
        print("Blackjack for the dealer! You lost.")
    elif player_score > computer_score:
        print(f"Your hand is bigger than the dealer's ({player_score} > {computer_score}). You won.")
    else:
        print(f"Your hand is less than the dealer's ({player_score} < {computer_score}). You lost.")
    
    should_continue_game = input("Do you wish to play another round? Type 'y' to restart or 'n' to leave the game.\n").lower()
    while should_continue_game not in valid_inputs:
        print("Invalid input.")
        should_continue_game = input().lower()
    
    if should_continue_game == 'n':
        print("Thanks for playing.\nBlackjack shutting down...")
        end_of_game = True



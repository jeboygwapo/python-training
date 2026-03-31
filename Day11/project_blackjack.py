import random

def initialize_game():
    dealer_list.clear()
    player_list.clear()

    d_list = dealer_draw_card()
    player_draw_card() 
    p_list = player_draw_card()

    p_score = sum(p_list)
    d_score = sum(d_list)
    
    return d_list, p_list, p_score, d_score 

def dealer_draw_card():
    card_drawn = random.choice(cards_list)
    if sum(dealer_list) > 11 :
        if card_drawn == 11:
            card_drawn = 1
            dealer_list.append(card_drawn)
    dealer_list.append(card_drawn)
    return dealer_list

def player_draw_card():
    card_drawn = random.choice(cards_list)
    if sum(player_list) > 11 :
        if card_drawn == 11:
            card_drawn = 1
            player_list.append(card_drawn)
    player_list.append(card_drawn)
    return player_list

def show_scores():
    print(f"Your cards: {player_list}, current score: {player_score}")
    print(f"Computer's first card: {dealer_score}")

def show_final_score(dealer_list, dealer_score, player_list, player_score):
    print(f"\nYour cards: {player_list}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_list}, final score: {dealer_score}")
    return False

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_list = []
player_list = []

session = True

while session:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game in ['y', 'n']:
        if start_game == 'y':
            dealer_list, player_list, player_score, dealer_score = initialize_game()
            show_scores() 
            in_game = True

            while in_game:
                another_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
                if another_card in ['y', 'n']:
                    if another_card == 'y':
                        player_list = player_draw_card()
                        player_score = sum(player_list)
                        
                        print(f"Your cards: {player_list}, current score: {player_score}")
                        print(f"Computer's first card: {dealer_score}")
                        if player_score > 21:
                            print("You went over. You lose...\n")
                            break
                    else:
                        dealer_list = dealer_draw_card()
                        dealer_score = sum(dealer_list)
                        while dealer_score < 17:
                            dealer_list = dealer_draw_card()
                            dealer_score = sum(dealer_list)
                        if player_score > dealer_score or dealer_score > 21:
                            in_game = show_final_score(dealer_list,dealer_score,player_list,player_score)
                            print("You win!\n")
                            break
                        elif dealer_score > player_score:
                            in_game = show_final_score(dealer_list,dealer_score,player_list,player_score)
                            print("You lose...\n")
                            break
                        else:
                            in_game = show_final_score(dealer_list,dealer_score,player_list,player_score)
                            print("Draw!\n")
                            break
                else:
                    print("Invalid choice, please try again.\n")

        else:
            print("See you again, thank you!\n")
            session = False
    else:
        print("Invalid input, please try again.\n")

            
    
    

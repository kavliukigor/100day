import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    player_card1 = random.choice(cards)
    cards.remove(player_card1)
    player_card2 = random.choice(cards)
    cards.remove(player_card2)
    dealer_card1 = random.choice(cards)
    cards.remove(dealer_card1)
    dealer_card2 = random.choice(cards)
    cards.remove(dealer_card2)
    dealer_score = dealer_card1 + dealer_card2
    player_score = player_card1 + player_card2
    print(f"Dealer card is {dealer_card1}")
    cont = input(f"Your cards {player_card1} {player_card2}\n Your score {player_score}\n Continue? 'Y' or 'N' ")
    return player_score, dealer_card1, dealer_card2, dealer_score, cont
    
def game_continue(player_score, cont):
    player_cart_add = random.choice(cards)
    cards.remove(player_cart_add)
    final_score = player_score + player_cart_add
    if final_score >21:
        print(f"Your new card is {player_cart_add} and score is {final_score}\n Too much")
        cont = 'N'
    else:
        cont = input(f"Your new card is {player_cart_add} and your score is {final_score}.\n One more card 'Y' or 'N' ")
        
    return cont, final_score

def dealer_fscore(dealer_score, dealer_card1, dealer_card2):
    print(f"Dealer cards is {dealer_card1} {dealer_card2} and score is {dealer_score}")
    while dealer_score <17:
        deal_new_card = random.choice(cards)
        cards.remove(deal_new_card)
        dealer_score += deal_new_card
        print(f"Dealer new card is {deal_new_card} and score is {dealer_score}")
    return dealer_score

game_start = input(f'Do you want start to play? "Yes" or "No" ')
if game_start == 'Yes':
    player_score, dealer_card1, dealer_card2, dealer_score, cont = game()
    final_score = player_score
    while cont == 'Y':
        cont, final_score = game_continue(final_score, cont)

    dealer_score =dealer_fscore(dealer_score, dealer_card1, dealer_card2)
    if final_score >21:
        print("Dealer win")
    elif final_score<=21 and dealer_score>21:
        print("You win")
    elif final_score>dealer_score:
        print("You win")
    elif final_score==dealer_score:
        print("Draw")
    elif final_score<dealer_score:
        print("Dealer win")        
else:
    print("Zrya")
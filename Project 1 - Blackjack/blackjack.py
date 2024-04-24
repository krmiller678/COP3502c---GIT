'''Project 1 - Blackjack'''
#This program is a simplified version of the casino game
#Important to note - Ace is 1, 2-10 correspond to face, Jack is 11, Queen 12, King 13
#Although face cards correspond to different rng values, they have value of 10

#Import modules needed for random generation
from p1_random import P1Random

#Setup P1Random class
rng = P1Random()

#Setup variables to initiate first game in loop, track stats
game_number = 1
continue_playing = True
player_wins = 0
dealer_wins = 0
ties = 0


while continue_playing == True:
    print(f'START GAME #{game_number}\n')

    #Deal first card of the game, random number [1,13]
    current_card = rng.next_int(13) + 1
    #Print card number or name, add in variable set to 10 for Face Cards
    if current_card == 1:
        print('Your card is a ACE!')
    elif current_card < 11:
        print(f'Your card is a {current_card}!')
    elif current_card == 11:
        print('Your card is a JACK!')
        current_card = 10
    elif current_card == 12:
        print('Your card is a QUEEN!')
        current_card = 10
    elif current_card == 13:
        print('Your card is a KING!')
        current_card = 10

    #Nested while loop to keep current hand going
    ongoing_hand = current_card
    print(f'Your hand is: {ongoing_hand}')
    print()

    while ongoing_hand <21:
        #Display Menu
        print('1. Get another card\n'
              '2. Hold hand\n'
              '3. Print statistics\n'
              '4. Exit\n')
        
        #Gather user input
        menu_select = input('Choose an option: ')
        print()

        #Validate menu select, if incorrect redisplay menu
        if menu_select in ['1','2','3','4']:
            menu_select = int(menu_select)
        else:
            print('Invalid input!')
            print('Please enter an integer value between 1 and 4.')
            print()
            continue

        #Actions to take based on menu_select
        if menu_select == 1:
            next_card = rng.next_int(13) + 1
            if next_card == 1:
                print('Your card is a ACE!')
            elif next_card < 11:
                print(f'Your card is a {next_card}!')
            elif next_card == 11:
                print('Your card is a JACK!')
                next_card = 10
            elif next_card == 12:
                print('Your card is a QUEEN!')
                next_card = 10
            elif next_card == 13:
                print('Your card is a KING!')
                next_card = 10
            ongoing_hand += next_card
            print(f'Your hand is: {ongoing_hand}')
            print()
        elif menu_select == 2:
            break
        elif menu_select == 3:
            print(f'Number of Player wins: {player_wins}\n'
                  f'Number of Dealer wins: {dealer_wins}\n'
                  f'Number of tie games: {ties}\n'
                  f'Total # of games played is: {ties+player_wins+dealer_wins}\n'
                  f'Percentage of Player wins: {player_wins / (ties+player_wins+dealer_wins) * 100}%\n')
            print()
        elif menu_select == 4:
            continue_playing = False
            break
    #Continue to start of original while loop if menu_select == 4
    if menu_select == 4:
        continue

    game_number += 1
    #Determine win, loss, or tie
    if ongoing_hand > 21:
        print('You exceeded 21! You lose.')
        print()
        dealer_wins += 1
    elif ongoing_hand == 21:
        print('BLACKJACK! You win!')
        print()
        player_wins += 1
    else:
        #Initialize random dealer hand, determine winner against dealer hand
        dealer_hand = rng.next_int(11) + 16

        if dealer_hand > 21:
            print(f'Dealer\'s hand: {dealer_hand}')
            print(f'Your hand is: {ongoing_hand}')
            print()
            print('You win!')
            print()
            player_wins += 1
        elif dealer_hand > ongoing_hand:
            print(f'Dealer\'s hand: {dealer_hand}')
            print(f'Your hand is: {ongoing_hand}')
            print()
            print('Dealer wins!')
            print()
            dealer_wins += 1
        elif dealer_hand == ongoing_hand:
            print(f'Dealer\'s hand: {dealer_hand}')
            print(f'Your hand is: {ongoing_hand}')
            print()
            print('It\'s a tie! No one wins!')
            print()
            ties += 1
        else:
            print(f'Dealer\'s hand: {dealer_hand}')
            print(f'Your hand is: {ongoing_hand}')
            print()
            print('You win!')
            print()
            player_wins += 1

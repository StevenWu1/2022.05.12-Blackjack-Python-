import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

try:
    answer = "yes"
    while answer == "yes":
        import random
        player_cards = []
        computer_cards = []
        player_action1 = 0
        player_action2 = 0
        player_action3 = 0
        player_action4 = 0
        player_action5 = 0

        def draw_card():
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            if sum(player_cards) > 11:
                cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            card = random.choice(cards)
            return card

        def draw_cards():
            cardss = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            if sum(computer_cards) > 11:
                cardss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            car = random.choice(cardss)
            return car

        def play_again():
            answer = input("Would you like to play again? (yes/no) ")
            if answer == "yes":
                os.system('clear')
                print("shuffling cards")
            else:
                quit()

        def end():
            while sum(computer_cards) < 17:
                computer_cards.append(draw_cards())
            if sum(computer_cards) > 21:
                print("You Win.")
                print("Computer cards: ", computer_cards)
                play_again()
            elif sum(computer_cards) > sum(player_cards):
                print("You Lose.")
                print("Computer cards: ", computer_cards)
                play_again()
            elif sum(computer_cards) < sum(player_cards):
                print("You Win!")
                print("Computer cards: ", computer_cards)
                play_again()
            elif sum(computer_cards) == sum(player_cards):
                print("You Tie!")
                print("Computer cards: ", computer_cards)
                play_again()
            else:
                print("You Lose")
                print("Computer cards: ", computer_cards)
                play_again()

        print(logo)
        start = input("Would you like to play? (yes/no) ")
        answer = start
        if start == "no":
            quit()

        for i in range(2):
            player_cards.append(draw_card())
            computer_cards.append(draw_cards())

        if sum(computer_cards) == 21:
            print("You lose. Computer has blackjack.")
            play_again()
        elif sum(player_cards) == 21:
            print("You win, You have blackjack.")
            play_again()
        elif sum(player_cards) == 21 and sum(computer_cards) == 21:
            print("Both have blackjack. Tie")
            play_again()

        print("Your cards are ", player_cards, "Computer's cards are",
              computer_cards[0])
        player_action1 = input("Would you like to hit or stand (yes/no)? ")

        if player_action1 == "yes":
            player_cards.append(draw_card())
            print("Your cards: ", player_cards)
            if sum(player_cards) > 21:
                print("You lose!")
                print("Computer cards: ", computer_cards)
                play_again()
            else:
                player_action2 = input(
                    "Would you like to hit or stand? (yes/no) ")
        elif player_action1 == "no":
            end()

        if player_action2 == "yes":
            player_cards.append(draw_card())
            print("Your cards: ", player_cards)
            if sum(player_cards) > 21:
                print("You lose!")
                print("Computer cards: ", computer_cards)
                play_again()
            else:
                player_action3 = input(
                    "Would you like to hit or stand? (yes/no) ")
        elif player_action2 == "no":
            end()

        if player_action3 == "yes":
            player_cards.append(draw_card())
            print("Your cards: ", player_cards)
            if sum(player_cards) > 21:
                print("You lose!")
                print("Computer cards: ", computer_cards)
                play_again()
            else:
                player_action4 = input(
                    "Would you like to hit or stand? (yes/no) ")
        elif player_action3 == "no":
            end()

        if player_action4 == "yes":
            player_cards.append(draw_card())
            print("Your cards: ", player_cards)
            if sum(player_cards) > 21:
                print("You lose!")
                print("Computer cards: ", computer_cards)
                play_again()
            else:
                player_action5 = input(
                    "Would you like to hit or stand? (yes/no) ")
        elif player_action4 == "no":
            end()

        if player_action5 == "yes":
            player_cards.append(draw_card())
            print("Your cards: ", player_cards)
            if sum(player_cards) > 21:
                print("You lose!")
                print("Computer cards: ", computer_cards)
                play_again()
            else:
                player_action6 = input(
                    "Would you like to hit or stand? (yes/no) ")
        elif player_action5 == "no":
            end()

    quit()
except:
    pass

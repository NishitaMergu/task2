# import random
#
# def play_game():
#     number_to_guess = random.randint(1, 200)
#     attempts = 0
#
#     print("Welcome to the Number Guessing Game!")
#     player_name = input("May I ask you for your name? ")
#     print(f"Hello, {player_name}! I'm thinking of a number between 1 and 200.")
#
#     while True:
#         guess = input("Guess the number: ")
#
#         if not guess.isdigit():
#             print("Please enter a valid number.")
#             continue
#
#         guess = int(guess)
#
#         if guess < 1 or guess > 200:
#             print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
#             continue
#
#         attempts += 1
#
#         if guess < number_to_guess:
#             print("The guess of the number that you have entered is too low. Try Again!")
#         elif guess > number_to_guess:
#             print("The guess of the number that you have entered is too high. Try Again!")
#         else:
#             print(f"Congratulations, {player_name}! You've guessed the number {number_to_guess} in {attempts} attempts!")
#             break
#
#     play_again = input("Do you want to play again, {}? (yes/no): ".format(player_name))
#     if play_again.lower() == 'yes':
#         play_game()
#     else:
#         print("Thanks for playing, {}! Goodbye!".format(player_name))
#
# play_game()



import random

def play_game():
    number_to_guess = random.randint(1, 200)
    attempts = 0

    print("May I ask you for your name?")
    player_name = input()
    print(f"{player_name}, we are going to play a game. I am thinking of a number between 1 and 200.")

    while True:
        guess = input("Go ahead. Guess!\nGuess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 200:
            print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("The guess of the number that you have entered is too low. Try Again!")
        elif guess > number_to_guess:
            print("The guess of the number that you have entered is too high. Try Again!")
        else:
            print(f"Nope. The number I was thinking of was {number_to_guess}")
            break

    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith('y'):
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

play_game()

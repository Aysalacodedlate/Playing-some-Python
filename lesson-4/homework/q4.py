#Number Guessing Game Create a simple number guessing game.
import random

def play_game():
    print("Let's start the number guessing game!")
    number_to_guess = random.randint(1, 100)  
    attempts = 10  
    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts remaining. Enter your guess: "))
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("That is correct!")
                return  
            attempts -= 1 
        except ValueError:
            print("O o!")
    print("You lost. The correct number was", number_to_guess)
    play_again = input("Want to play again? (Y/YES/y/yes/ok): ").strip().lower()
    if play_again in ['y', 'yes', 'ok']:
        play_game()  
    else:
        print("Oh, okay!")
play_game()

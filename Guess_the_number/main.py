from sympy import ask
from display_info import logo, instructions
from random import randint
import os

clear = lambda: os.system("clear" if os.name == "posix" else "cls")


def ask_to_play():
    want_to_play = input("Do you want to play 'y' or 'n' : ").lower()
    if want_to_play == "y":
        return True
    elif want_to_play == "n":
        return False
    else:
        print("invalid input!")
        ask_to_play()


def choose_mode():
    mode = input("Choose mode 'e' for easy 'd' for difficult : ").lower()
    if mode == "e":
        return 10
    elif mode == "d":
        return 5
    else:
        print("invalid input!")
        choose_mode()


def game(lives):
    for i in range(lives):
        print(f"You have {lives-i} lives remaining to guess the number")
        guessed_number = int(input("Guess the number : "))
        if guessed_number > number_generated:
            print("Too High!")
        elif guessed_number < number_generated:
            print("Too Low!")
        else:
            print("You Win!")
            break


while True:
    want_to_play = ask_to_play()
    if want_to_play is False:
        break
    else:
        clear()
        print(logo)
        instructions()
        lives = (choose_mode())
        number_generated = randint(1, 100)
        game(lives)

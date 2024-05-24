import random


def choose_mode():
    chosen_mode = input("Choose your mode, easy or hard (e/h): ").strip().lower()
    return 10 if chosen_mode == "e" else 5


def number_randomizer():
    goal_number = random.randint(1, 100)
    return goal_number


def pick_number():
    chosen_number = int(input("Choose a number from 1 to 100: "))
    return chosen_number


def game():
    lives = choose_mode()
    goal_number = number_randomizer()
    # while lives > 0:


print(pick_number())

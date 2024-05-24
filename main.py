import random


def choose_mode():
    chosen_mode = input("Choose your mode, easy or hard (e/h): ").strip().lower()
    return 10 if chosen_mode == "e" else 5


def pick_number():
    goal_number = random.randint(1, 100)
    return goal_number


def game():
    lives = choose_mode()
    goal_number = pick_number()

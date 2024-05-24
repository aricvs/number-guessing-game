import random


def choose_mode():
    chosen_mode = input("Choose your mode, easy or hard (e/h): ").strip().lower()
    return 0 if chosen_mode == "e" else 1


def pick_number():
    goal_number = random.randint(1, 100)
    return goal_number

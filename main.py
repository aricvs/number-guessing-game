import random


def choose_mode():
    chosen_mode = input("Choose your mode, easy or hard (e/h): ").strip().lower()
    return 10 if chosen_mode == "e" else 5


def number_randomizer():
    goal_number = random.randint(1, 100)
    print(goal_number)  # for testing, delete later
    return goal_number


def pick_number():
    chosen_number = int(input("Choose a number from 1 to 100: "))
    return chosen_number


def compare_numbers(pick, goal):
    if pick == goal:
        # print("Equals")  # for testing, delete later
        return 0
    if pick < goal:
        # print("Lower")  # for testing, delete later
        return 1
    if pick > goal:
        # print("Higher")  # for testing, delete later
        return 2


def game():
    lives = choose_mode()
    goal_number = number_randomizer()
    while lives > 0:
        picked = pick_number()


print(compare_numbers(pick_number(), number_randomizer()))

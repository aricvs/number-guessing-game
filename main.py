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


def compare_numbers(pick, goal):
    if pick == goal:
        return 0
    if pick < goal:
        return 1
    if pick > goal:
        return 2


def game():
    lives = choose_mode()
    goal_number = number_randomizer()

    while lives > 0:
        print(f"Lives remaining: {lives}")
        picked = pick_number()
        result = compare_numbers(picked, goal_number)

        if result == 0:
            print("You win!")
            break
        if result == 1:
            print("Too low!")
            lives -= 1
        if result == 2:
            print("Too high!")
            lives -= 1

    if lives == 0:
        print("You lose!")


game()

import numpy as np
import secrets

def next_step() -> str:
    directions = ['up', 'down', 'right', 'left']
    return secrets.choice(directions)


def random_walk(n):
    home = [0, 0]
    current_pos = [0, 0]
    count = 0
    result = 0

    while count != n:
        next_direction = next_step()
        if next_direction == "up":
            current_pos[1] += 1
        elif next_direction == "down":
            current_pos[1] -= 1
        elif next_direction == "right":
            current_pos[0] += 1
        elif next_direction == "left":
            current_pos[0] -= 1

        count += 1

    if current_pos[0] == home[0] and current_pos[1] == home[1]:
        result = 1
    return result


def random_walk_trials(n, t):
    trials = 0
    result = 0
    while trials != t:
        result += random_walk(n)
        trials += 1
    return result

def print_trial(n,t):
    print("n =", n, "with", t, "trials", "results in", random_walk_trials(n,t))

# print_trial(10,100)
# print_trial(10,10000)
# print_trial(10,1000000)
# print(" ")
# print_trial(30,100)
# print_trial(30,10000)
# print_trial(30,1000000)
# print(" ")
# print_trial(50,100)
# print_trial(50,10000)
# print_trial(50,1000000)
# print(" ")
# print_trial(100,100)
# print_trial(100,10000)
# print_trial(100,1000000)


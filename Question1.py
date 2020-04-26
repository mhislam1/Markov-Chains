import numpy as np
import secrets

def next_step()->str:
    directions = ['up', 'down', 'right', 'left']
    return secrets.choice(directions)
#
# def random_walk(n)->int:
#     # Creates nxn coordinate plane
#     nx, ny = (n + 1, n + 1)
#     x = np.linspace(-n, n, nx)
#     y = np.linspace(-n, n, ny)
#     xv, yv = np.meshgrid(x, y, sparse=False, indexing="xy")
#     x_hor = 0
#     x_ver = 0
#     y_hor = 0
#     y_ver = 0
#     home = xv[x_hor, x_ver], yv[y_hor, y_ver]
#     current_pos = home
#     count = 0
#     result = 0
#     while count != n:
#         next_direction = next_step()
#         if next_direction == "up":
#             current_pos = yv[y_hor+1,y_ver+1]
#         elif  next_direction == "down":
#             current_pos = yv[y_hor-1,y_ver-1]
#         elif next_direction == "right":
#             current_pos = xv[x_hor+1, x_ver+1]
#         elif next_direction == "left":
#             current_pos = xv[x_hor - 1, x_ver - 1]
#         count += 1
#     if current_pos == all(home):
#         result = 1
#     return result
#
#
# def random_walk_trials(n,t):
#     trials = 0
#     result = 0
#     while trials != t:
#         result += random_walk(n)
#         trials += 1
#     return result
#
# for i in range(0,50):
#     print(random_walk(5))
#


def rand_walk(n):
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

    if current_pos[0] == home [0] and current_pos[1] == home[1]:
        result = 1
    return result


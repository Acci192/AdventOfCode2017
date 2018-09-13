import numpy as np
def to_string_pos(a, b):
    return str(a) + "," + str(b)


def create_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(".")
        grid.append(row)
    return grid

import time
start_time = time.time()

file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()



input = input.split("\n")

infected = []
flagged = []
weakened = []
small_grid = []
for line in input:
    small_grid.append(list(line))

width = 675
height = 675


grid = create_grid(675)


for x in range(25):
    for y in range(25):
        grid[325+y][325+x] = small_grid[y][x]


x_pos = int(width/2)
y_pos = int(height/2)


direction = 0

counter = 0
for i in range(10000000):

    typ = grid[y_pos][x_pos]
    if typ == "#":
        direction = (direction + 1) % 4
        grid[y_pos][x_pos] = "F"
    elif typ == "F":
        direction = (direction + 2) % 4
        grid[y_pos][x_pos] = "."
    elif typ == ".":
        direction = (direction - 1) % 4
        grid[y_pos][x_pos] = "W"
    elif typ == "W":
        grid[y_pos][x_pos] = "#"
        counter += 1
    else:
        print("BAD THINGS")

    if direction == 0:
        y_pos -= 1
    elif direction == 1:
        x_pos += 1
    elif direction == 2:
        y_pos += 1
    elif direction == 3:
        x_pos -= 1
    else:
        print("MOVING ERROR")
    
print ("My program took", time.time() - start_time, "to run")
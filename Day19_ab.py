import re

file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

input = input.split('\n')
print(len(input[0]))

grid = []
for s in input:
    row = []
    for i in range(200):
        row.append(s[i])
    grid.append(row)
    
pos_x, pos_y = 163, 0


# Up = 0, right = 1, down = 2, left = 3
direction = 2

order = []
letter = re.compile("[A-Z]")
def change_dir(grid, pos_x, pos_y, direction):
    regex = re.compile("[A-Z\-\|]")
    if(regex.match(" ")):
        print("MATCH" )
    if direction == 0 or direction == 2:
        if pos_x != 199:
            if regex.match(grid[pos_y][pos_x + 1]):
                return 1
        if pos_x != 0:
            if regex.match(grid[pos_y][pos_x-1]):
                return 3
    else:
        if pos_y != 0:
            if regex.match(grid[pos_y-1][pos_x]):
                return 0
        
        if pos_y != 199:
            if regex.match(grid[pos_y+1][pos_x]):
                return 2
    
    
    return -1
turn = 0
while True:
   # print("X:", pos_x, "Y:", pos_y)
   # print(grid[pos_y][pos_x])
    if direction == 0:
        pos_y -= 1
    elif direction == 1:
        pos_x +=1
    elif direction == 2:
        pos_y +=1
    elif direction == 3:
        pos_x -=1
    else:
        break
    
    if grid[pos_y][pos_x] == "+":
        #print("Dir:", direction)
        direction = change_dir(grid, pos_x, pos_y, direction)
        #print("new dir:", direction)
    if letter.match(grid[pos_y][pos_x]):
        if(grid[pos_y][pos_x] == "Y"):
            print(turn)
        order.append(grid[pos_y][pos_x])
    if grid[pos_y][pos_x] == " ":
        break
    turn +=1
    
print("".join(order))
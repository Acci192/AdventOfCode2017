def to_string_pos(a, b):
    return str(a) + "," + str(b)


file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

input = input.split("\n")

infected = []
flagged = []
weakened = []
grid = []
for line in input:
    grid.append(list(line))


width = len(grid[0])
height = len(grid)

for c in range(width):
    for r in range(height):
        if grid[r][c] == "#":
            infected.append(to_string_pos(r,c))


x_pos = int(width/2)
y_pos = int(height/2)

direction = 0

counter = 0
for i in range(10000):
    curr_pos = to_string_pos(y_pos,x_pos)  
    if curr_pos in infected:
        direction = (direction + 1) % 4
        infected.remove(curr_pos)
    else:
        direction = (direction - 1) % 4
        infected.append(curr_pos)
        counter +=1
        

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
    
    
def move_right(pos):
    return pos + 1

def move_left(pos):
    return pos - 1


space = [0] * 1000000
pos = len(space)//2
state = 0

for i in range(12368930):
    # State A
    if state == 0:
        if space[pos] == 1:
            space[pos] = 0
            pos = move_right(pos)
            state = 2
        else:
            space[pos] = 1
            pos = move_right(pos)
            state = 1
    elif state == 1:
        if space[pos] == 1:
            space[pos] = 0
            pos = move_right(pos)
            state = 3
        else:
            pos = move_left(pos)
            state = 0
    elif state == 2:
        if space[pos] == 1:
            pos = move_right(pos)
            state = 0
        else:
            space[pos] = 1
            pos = move_right(pos)
            state = 3
    elif state == 3:
        if space[pos] == 1:
            space[pos] = 0
            pos = move_left(pos)
            state = 3
        else:
            space[pos] = 1
            pos = move_left(pos)
            state = 4
    elif state == 4:
        if space[pos] == 1:
            pos = move_left(pos)
            state = 1
        else:
            space[pos] = 1
            pos = move_right(pos)
            state = 5
    elif state == 5:
        if space[pos] == 1:
            pos = move_right(pos)
            state = 4
        else:
            space[pos] = 1
            pos = move_right(pos)
            state = 0

print(sum(space))
input = 337
pos = 0
pos1 = 0
for i in range (1,50000000):
    pos = ((pos+input)% i) +1
    if(pos == 1):
        pos1 = i

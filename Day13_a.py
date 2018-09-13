file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

def day13_a(input):
    input = input.split("\n")
    firewall = {}
    for line in input:
        depth, ran = line.split(": ")
        firewall[int(depth)] = int(ran)
        

    size = max(firewall.keys())
    positions = []
    move_down = []
    for i in range(size+1):
        if i in firewall:
            positions.append(0)
            move_down.append(True)
        else:
            positions.append(-1)
            move_down.append(False)
    
    pack_pos = 0
    loss = 0
    for i in range(size+1):
        if(positions[pack_pos] == 0):
            loss += i*firewall[i]
        #update firewall
        for j in range(len(positions)):
            if positions[j] >= 0:
                if move_down[j]:
                    positions[j] += 1
                    if positions[j] == firewall[j]-1:
                        move_down[j] = False
                else:
                    positions[j] -= 1
                    if positions[j] == 0:
                        move_down[j] = True
        pack_pos += 1
    
    print(loss)
                
    
day13_a(input)
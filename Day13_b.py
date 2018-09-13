file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

def day13_b(input):
    input = input.split("\n")
    firewall = {}
    for line in input:
        depth, ran = line.split(": ")
        firewall[int(depth)] = (int(ran)-1)*2
        
    size = max(firewall.keys())
    x = 0
    sol = False
    while not sol:
        sol = True
        for i in range(size+1):  
            if i in firewall:
                if (i + x) % firewall[i] == 0:
                    sol = False
                    break
        
        x += 1
        if i == size+1:
            break
        
    print(x-1)
                
day13_b(input)
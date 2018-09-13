    def spin(size, programs):
    temp1 = programs[16-size:]
    temp2 = programs[:16-size]
    return temp1 + temp2

def swap(pos1, pos2, programs):
    temp = programs[pos1]
    programs[pos1] = programs[pos2]
    programs[pos2] = temp
    return programs

def partner(char1, char2, programs):
    pos1 = programs.index(char1)
    pos2 = programs.index(char2)
    return swap(pos1, pos2, programs)


file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

programs = []
for i in range(16):
    programs.append(chr(i+97))

instructions = input.split(",")
for x in range(1):
    if(x % 100000 == 0):
        print(x)
    
    
    for i in instructions:
        if(i[0] == 's'):
            size = int(i[1:])
            programs = spin(size, programs)
        elif(i[0] == 'x'):
            temp = i.split("/")
            pos1 = int(temp[0][1:])
            pos2 = int(temp[1])
            programs = swap(pos1, pos2, programs)
        elif(i[0] == 'p'):
            programs = partner(i[1],i[3], programs)
    
result = ''.join(programs)
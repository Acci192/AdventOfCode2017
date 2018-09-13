file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

def day12_a(input):
    program = {}
    input = input.split("\n")
    for s in input:
        prog, con = s.split(" <-> ")
        prog = int(prog)
        program[prog] = list(map(int,con.split(",")))
    
    connected = [0]
    i = 0
    while(i < len(connected)):
        for k in program:
            if connected[i] in program[k]:
                if k not in connected:
                    connected.append(k)
        i += 1
    print(len(connected))
day12_a(input)
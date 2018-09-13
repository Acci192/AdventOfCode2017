file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

def day12_b(input):
    program = {}
    input = input.split("\n")
    for s in input:
        prog, con = s.split(" <-> ")
        prog = int(prog)
        program[prog] = list(map(int,con.split(",")))
        
        
    counter = 0
    while len(program) > 0:
        connected = next(iter(program.values()))
        i = 0
        while(i < len(connected)):
            for k in program:
                if connected[i] in program[k]:
                    if k not in connected:
                        connected.append(k)
            i += 1
        for c in connected:
            program.pop(c)
        counter += 1
    print(counter)

day12_b(input)
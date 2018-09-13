registers = {}
for i in range(16):
    registers[chr(i+97)] = 0


file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

temp_instructions = input.split("\n")
instructions = []
for i in temp_instructions:
    instructions.append(i.split())

for i in instructions:
    if (len(i) >2):
        if "-" in i[2] or i[2].isdigit():
            i[2] = int(i[2])
        
frequencies = []
freq = None
pc = 0
while pc >=0 and pc < len(instructions):
    print(instructions[pc])
    if(instructions[pc][0] == "snd"):
        frequencies.append(int(registers[instructions[pc][1]]))
    elif(instructions[pc][0] == "set"):
        if(isinstance(instructions[pc][2], int)):
            registers[instructions[pc][1]] = int(instructions[pc][2])
        else:
            registers[instructions[pc][1]] = registers[instructions[pc][2]]
    elif(instructions[pc][0] == "add"):
        if(isinstance(instructions[pc][2], int)):
            registers[instructions[pc][1]] += int(instructions[pc][2])
        else:
            registers[instructions[pc][1]] = int(registers[instructions[pc][1]]) + int(registers[instructions[pc][2]])
    elif(instructions[pc][0] == "mul"):
        if(isinstance(instructions[pc][2], int)):
            registers[instructions[pc][1]] *= int(instructions[pc][2])
        else:
            registers[instructions[pc][1]] = int(registers[instructions[pc][1]]) * int(registers[instructions[pc][2]])
    elif(instructions[pc][0] == "mod"):
        if(isinstance(instructions[pc][2], int)):
            registers[instructions[pc][1]] %= int(instructions[pc][2])
        else:
            registers[instructions[pc][1]] = int(registers[instructions[pc][1]]) % int(registers[instructions[pc][2]])
    elif(instructions[pc][0] == "rcv"):
        if(int(registers[instructions[pc][1]]) != 0):
            print(frequencies[len(frequencies) - 1])
            break
    
    if(instructions[pc][0] == "jgz"):
        if(int(registers[instructions[pc][1]]) != 0):
            if(isinstance(instructions[pc][2], int)):
                pc += int(instructions[pc][2])
            else:
                pc += int(registers[instructions[pc][2]])
        else:
            pc += 1
    else:
        pc += 1
        
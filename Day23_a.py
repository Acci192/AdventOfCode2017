import re
def getValue(x, registers):
    if type(x) is int:
        return x
    else:
        return registers[x]

registers = {}
for i in range(10):
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
        if "-" in i[1] or i[1].isdigit():
            i[1] = int(i[1])

counter = 0
pc = 0
while pc >=0 and pc < len(instructions):

    ins = instructions[pc]

    if(ins[0] == "set"):
        registers[ins[1]] = getValue(ins[2], registers)
        pc += 1
    elif(ins[0] == "mul"):
        registers[ins[1]] *= getValue(ins[2], registers)
        pc += 1
        counter += 1
    elif(ins[0] == "sub"):
        registers[ins[1]] -= getValue(ins[2], registers)
        pc += 1
    elif(ins[0] == "jnz"):
        if(getValue(ins[1], registers) != 0):
            pc += getValue(ins[2], registers)
        else:
            pc += 1

    

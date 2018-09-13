registers_0 = {}
for i in range(16):
    registers_0[chr(i+97)] = 0
registers_1 = {}
for i in range(16):
    registers_1[chr(i+97)] = 0

registers_0['p'] = 0
registers_1['p'] = 1

channel_0 = []
channel_1 = []

file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

temp_instructions = input.split("\n")
instructions = []
for i in temp_instructions:
    instructions.append(i.split())

for i in instructions:
    if i[1].isdigit():
        i[1] = int(i[1])
    if (len(i) >2):
        if "-" in i[2] or i[2].isdigit():
            i[2] = int(i[2])
        
frequencies = []
freq = None
pc_0 = 0
pc_1 = 0

running_0 = True
running_1 = True

waiting_0 = False
waiting_1 = False

counter = 0
while running_0 or running_1:
    
    if(running_0):
        if(instructions[pc_0][0] == "snd"):
            channel_1.append(int(registers_0[instructions[pc_0][1]]))
            pc_0 += 1
        elif(instructions[pc_0][0] == "set"):
            if(isinstance(instructions[pc_0][2], int)):
                registers_0[instructions[pc_0][1]] = int(instructions[pc_0][2])
            else:
                registers_0[instructions[pc_0][1]] = registers_0[instructions[pc_0][2]]
            pc_0 += 1
        elif(instructions[pc_0][0] == "add"):
            if(isinstance(instructions[pc_0][2], int)):
                registers_0[instructions[pc_0][1]] += int(instructions[pc_0][2])
            else:
                registers_0[instructions[pc_0][1]] = int(registers_0[instructions[pc_0][1]]) + int(registers_0[instructions[pc_0][2]])
            pc_0 += 1
        
        elif(instructions[pc_0][0] == "mul"):
            if(isinstance(instructions[pc_0][2], int)):
                registers_0[instructions[pc_0][1]] *= int(instructions[pc_0][2])
            else:
                registers_0[instructions[pc_0][1]] = int(registers_0[instructions[pc_0][1]]) * int(registers_0[instructions[pc_0][2]])
            pc_0 += 1
        elif(instructions[pc_0][0] == "mod"):
            if(isinstance(instructions[pc_0][2], int)):
                registers_0[instructions[pc_0][1]] %= int(instructions[pc_0][2])
            else:
                registers_0[instructions[pc_0][1]] = int(registers_0[instructions[pc_0][1]]) % int(registers_0[instructions[pc_0][2]])
            pc_0 += 1
        elif(instructions[pc_0][0] == "rcv"):
            if(len(channel_0) == 0):
                waiting_0 = True
                if(waiting_0 and waiting_1):
                    break
            else:
                registers_0[instructions[pc_0][1]] = channel_0.pop(0)
                pc_0 += 1
                waiting_0 = False
        if(instructions[pc_0][0] == "jgz"):
            if(isinstance(instructions[pc_0][1], int)):
                if(instructions[pc_0][1] > 0):
                    if(isinstance(instructions[pc_0][2], int)):
                        pc_0 += int(instructions[pc_0][2])
                    else:
                        pc_0 += int(registers_0[instructions[pc_0][2]])
                else:
                    pc_0 += 1
            else:
                if(int(registers_0[instructions[pc_0][1]]) > 0):
                    #print(registers_0[instructions[pc_0][1]])
                    if(isinstance(instructions[pc_0][2], int)):
                        pc_0 += int(instructions[pc_0][2])
                    else:
                        pc_0 += int(registers_0[instructions[pc_0][2]])
                else:
                    pc_0 += 1
        if(pc_0 >= 0 and pc_0 < len(instructions)):
            running_0 = True
        else:
            running_0 = False
            waiting_0 = True
    
    if(running_1):
       # print(instructions[pc_1])
        if(instructions[pc_1][0] == "snd"):
            channel_0.append(int(registers_1[instructions[pc_1][1]]))
            
            counter +=1
            pc_1 += 1
        elif(instructions[pc_1][0] == "set"):
            if(isinstance(instructions[pc_1][2], int)):
                registers_1[instructions[pc_1][1]] = int(instructions[pc_1][2])
            else:
                registers_1[instructions[pc_1][1]] = registers_1[instructions[pc_1][2]]
            pc_1 += 1
        elif(instructions[pc_1][0] == "add"):
            if(isinstance(instructions[pc_1][2], int)):
                registers_1[instructions[pc_1][1]] += int(instructions[pc_1][2])
            else:
                registers_1[instructions[pc_1][1]] = int(registers_1[instructions[pc_1][1]]) + int(registers_1[instructions[pc_1][2]])
            pc_1 += 1
        
        elif(instructions[pc_1][0] == "mul"):
            if(isinstance(instructions[pc_1][2], int)):
                registers_1[instructions[pc_1][1]] *= int(instructions[pc_1][2])
            else:
                registers_1[instructions[pc_1][1]] = int(registers_0[instructions[pc_1][1]]) * int(registers_1[instructions[pc_1][2]])
            pc_1 += 1
        elif(instructions[pc_1][0] == "mod"):
            if(isinstance(instructions[pc_1][2], int)):
                registers_1[instructions[pc_1][1]] %= int(instructions[pc_1][2])
            else:
                registers_0[instructions[pc_1][1]] = int(registers_0[instructions[pc_1][1]]) % int(registers_1[instructions[pc_1][2]])
            pc_1 += 1
        elif(instructions[pc_1][0] == "rcv"):
            if(len(channel_1) == 0):
                waiting_1 = True
                if(waiting_0 and waiting_1):
                    break
            else:
                registers_1[instructions[pc_1][1]] = channel_1.pop(0)
                pc_1 += 1
                waiting_0 = False
        if(instructions[pc_1][0] == "jgz"):
            if(isinstance(instructions[pc_1][1], int)):
             #   print("HEHE")
                if(instructions[pc_1][1] > 0):
                    if(isinstance(instructions[pc_1][2], int)):
                        pc_1 += int(instructions[pc_1][2])
                    else:
                        pc_1 += int(registers_1[instructions[pc_1][2]])
                else:
                    pc_1 += 1
            else:
                if(int(registers_1[instructions[pc_1][1]]) > 0):
                    if(isinstance(instructions[pc_1][2], int)):
                        pc_1 += int(instructions[pc_1][2])
                    else:
                        pc_1 += int(registers_1[instructions[pc_1][2]])
                else:
                    pc_1 += 1
        if(pc_1 >= 0 and pc_1 < len(instructions)):
            running_1 = True
        else:
            running_1 = False
            waiting_1 = True
    
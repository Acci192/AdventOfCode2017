file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()
def day11_a(input):
    ins = input.split(",")
    n = 0
    ne = 0
    nw = 0
    s = 0
    se = 0
    sw = 0
    temp_max = 0
    for i in ins:
        if i == "n":
            if s > 0:
                s -= 1
            elif se > 0:
                se -= 1
                ne += 1
            elif sw > 0:
                sw -= 1
                nw += 1
            else: 
                n += 1
        if i == "ne":
            if sw > 0:
                sw -= 1
            elif s > 0:
                s -= 1
                se += 1
            elif nw > 0:
                nw -= 1
                n += 1
            else:
                ne += 1
        if i == "nw":
            if se > 0:
                se -= 1
            elif s > 0:
                s -= 1
                sw += 1
            elif ne > 0:
                ne -= 1
                n += 1
            else:
                nw += 1
        if i == "s":
            if n > 0:
                n -= 1
            elif ne > 0:
                ne -= 1
                se += 1
            elif nw > 0:
                nw -= 1
                sw += 1
            else: 
                s += 1
        if i == "se":
            if nw > 0:
                nw -= 1
            elif n > 0:
                n -= 1
                ne += 1
            elif sw > 0:
                sw -= 1
                s += 1
            else:
                se += 1
        if i == "sw":
            if ne > 0:
                ne -= 1
            elif n > 0:
                n -= 1
                nw += 1
            elif se > 0:
                se -= 1
                s += 1
            else:
                sw += 1
        temp = n+ne+nw+s+se+sw
        if temp > temp_max:
            temp_max = temp
    
    
    
    print(temp)
    print(temp_max)
day11_a(input)


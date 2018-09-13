file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

def day10_b(input):
    size = 256
    lis = list(range(size))
    ins = create_ins(input)
    skip = 0
    start = 0
    for j in range(64):
        for i in ins:
            if i == 1 or i == 0:
                start += (i + skip)
                start = start % size
                skip += 1
            else:
                end = (start + i - 1) % size
                if end > start:
                    temp_list = lis[start:end+1]
                    temp_list.reverse()
                    lis[start:end+1] = temp_list
                    start += (i + skip)
                    start = start % size
                    skip += 1
                else:
                    temp_list = lis[start:]
                    
                    temp_list.extend(lis[:end + 1])
                    temp_list.reverse()
                    temp_diff = size - start
                    lis[start:] = temp_list[:temp_diff]
                    lis[:end+1] = temp_list[temp_diff:]
                    start += (i + skip)
                    start = start % size
                    skip += 1
    
    new_list = []
    i = 0
    while i < size:
        dense = lis[i]
        i += 1
        for j in range(15):
            dense = dense ^ lis[i]
            i += 1
        new_list.append(dense)
    
    result = ""
    for i in new_list:
        temp = hex(i)[2:]
        if len(temp) == 1:
            temp = "0" + temp
        result = result + temp
    print(result)

def create_ins(s):
    ins = []
    s.strip()
    for c in s:
        ins.append(ord(c))
    ins.extend([17, 31, 73, 47, 23])
    return ins

day10_b(input)


test = hex(64)[2:]

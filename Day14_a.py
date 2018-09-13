
def day10_b(input):
    rows = []
    for x in range(128):
        new_input = input + '-' + str(x)
        size = 256
        lis = list(range(size))
        ins = create_ins(new_input)
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
        rows.append(result)
    temp_result = ""
    for r in rows:
        temp_result = temp_result + hex_to_bin(r) + '\n'
    print(temp_result.count("1"))
    return temp_result

def create_ins(s):
    ins = []
    s.strip()
    for c in s:
        ins.append(ord(c))
    ins.extend([17, 31, 73, 47, 23])
    return ins

def hex_to_bin(s):
    hex2bin_map = {
   "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",    
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "a":"1010",
   "b":"1011",
   "c":"1100",
   "d":"1101",
   "e":"1110",
   "f":"1111",
   }
    hex_num=s
    return "".join(hex2bin_map[i] for i in hex_num)

temp = day10_b("amgozmfv")
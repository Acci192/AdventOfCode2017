file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

def day10_a(input):
    size = 256
    lis = list(range(size))
    ins = list(map(int, input.split(",")))
    print(lis)
    skip = 0
    start = 0
    
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
    print(lis[0] * lis[1])
    
day10_a(input)
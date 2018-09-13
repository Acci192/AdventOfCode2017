import numpy as np
import sys
sys.setrecursionlimit(1000) # 10000 is an example, try with different values
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

def update(i,j, visited, graph):
    rowN = [-1, 0, 1, 0]
    colN = [0, -1, 0, 1]
    visited[i,j] = True
    

    for x in range(4):
        r = rowN[x]
        if(i+r >= 0 and i+r < 128):
            c = colN[x]
            if(j+c >= 0 and j+c < 128):
                if(graph[i+r][j+c] == "1" and visited[i+r,j+c] ==False):
                    update(i+r, j+c, visited, graph)

input = "amgozmfv"
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
graph = []
for r in rows:
    graph.append(list(hex_to_bin(r)))

visited = np.zeros((128,128), dtype=bool)

counter = 0
for i in range(128):
    for j in range(128):
        if(visited[i,j] == False and graph[i][j] == "1"):
            counter += 1
            
            update(i,j,visited, graph)
            print("Hello")
            

print(counter)                




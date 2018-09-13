import copy

file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

input = input.split("\n")


components = {}

for i in range(55):
    components[i] = []
bridges = []
temp_bridge = []
connection = 0



for line in input:
    temp = line.split("/")
    a = int(temp[0])
    b = int(temp[1])
    if a != b:
        components[a].append(b)
        components[b].append(a)


def rec(components, bridges, temp_bridge, connection):
    comp = copy.deepcopy(components)
    temp = copy.deepcopy(temp_bridge)
    con = copy.deepcopy(connection)
    if len(components[con]) > 0:
        for c in components[con]:
            comp[con].remove(c)
            comp[c].remove(con)
            temp.append(c)
            rec(comp, bridges, temp, c)
            temp.remove(c)
            comp[con].append(c)
            comp[c].append(con)
    else:
        bridges.append(temp)
        
rec(components, bridges, temp_bridge, connection)

weight = [0] * 27214
for i in range(len(bridges)):
    weight[i] = sum(bridges[i]) * 2 - bridges[i][-1]
    if(46 in bridges[i]):
        weight[i] += 92
    if(38 in bridges[i]):
        weight[i] += 76
    if(40 in bridges[i]):
        weight[i] += 80
    if(29 in bridges[i]):
        weight[i] += 58
    if(6 in bridges[i]):
        weight[i] += 12
    if(39 in bridges[i]):
        weight[i] += 78
    if(28 in bridges[i]):
        weight[i] += 56

print(max(weight))

length = [0] * 27214
for i in range(len(bridges)):
    length[i] = len(bridges[i])
    if(46 in bridges[i]):
        length[i] += 1
    if(38 in bridges[i]):
        length[i] += 1
    if(40 in bridges[i]):
        length[i] += 1
    if(29 in bridges[i]):
        length[i] += 1
    if(6 in bridges[i]):
        length[i] += 1
    if(39 in bridges[i]):
        length[i] += 1
    if(28 in bridges[i]):
        length[i] += 1

print(max(length))

print(length.count(36))
maxx = 0
for i in range(len(bridges)):
    if(length[i] == 36):
        print(weight[i])
        print(i)
        if(weight[i] > maxx):
            maxx = weight[i]
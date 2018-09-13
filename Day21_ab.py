def unflatten(flat):
    output = []
    flat = flat.split("/")
    for r in flat:
        output.append(list(r))
    return output

def flatten(matrix):
    output = ""
    for row in matrix:
        output += "".join(row)
        output += "/"
    return output[:-1]

def rotate(matrix):
    return list(zip(*matrix[::-1]))

def flip(matrix):
    return list(map(reversed, matrix))

def display(image):
    dis = ""
    for row in image:
        dis += "".join(row)
        dis += "\n"
    print(dis)

file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()

input = input.split("\n")

rules = {}

for line in input:
    temp = line.split(" => ")
    img = temp[0]
    out = temp[1]
    size = len(img.split("/"))
    rules[img] = out
    for rotations in range(4):
        for flips in range(2):
            new_img = unflatten(img)
            for i in range(rotations):
                new_img = rotate(new_img)
            for i in range(flips):
                new_img = flip(new_img)
            rules[flatten(new_img)] = out

image = [[".","#","."],
         [".",".","#"],
         ["#","#","#"]]

for iterations in range(18):
    temp_image = []
    size = len(image)
    #display(image)
    if(size % 2 == 0):
        for row in range(int(size/2)):
            temp_row = []
            for col in range(int(size/2)):
                temp = []
                for r in range(2):
                    temp.append([])
                    for c in range(2):
                        temp[r].append(image[r + row*2][c + col*2])
                #print(temp)
                flat = flatten(temp)
                temp_row.extend(unflatten(rules[flat]))
                #print(temp_row)
                
            for j in range(3):
                com_row = []
                for k in range(int(size/2)):
                    com_row.extend(temp_row[k*3 + j])
                temp_image.append(com_row)
        #display(temp_image)
        
    elif(size % 3 == 0):
        for row in range(int(size/3)):
            temp_row = []
            for col in range(int(size/3)):
                temp = []
                for r in range(3):
                    temp.append([])
                    for c in range(3):
                        temp[r].append(image[r + row*3][c + col*3])
                #print(temp)
                flat = flatten(temp)
                temp_row.extend(unflatten(rules[flat]))
                #print(temp_row)
                
            for j in range(4):
                com_row = []
                for k in range(int(size/3)):
                    com_row.extend(temp_row[k*4 + j])
                temp_image.append(com_row)
        #display(temp_image)
    image = temp_image
    #print("ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ")

count = 0
for row in image:
    count += row.count("#")

display(image)
print(count)


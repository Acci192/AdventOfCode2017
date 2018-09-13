def day2b(input):
    splitted_input = input.split("\n")
    summ = 0
    correct_input = []
    for i in splitted_input:
        temp = i
        correct_input.append(correct_input.split())
    for row in correct_input:
        for i in range(len(row) - 1):
            x = row[i]
            for j in range(i + 1, len(row)):
                y = row[j]
                if(x < y):
                    if(int(y/x) == y/x):
                        summ += y/x
                elif(y < x):
                    if(int(x/y) == x/y):
                        summ += x/y
                else:
                    summ += 1
    print(summ)
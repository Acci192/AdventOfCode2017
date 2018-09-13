input = 337

buffer = [0]
pos = 0
for i in range (1,2018):
    temp = (pos + input) % (len(buffer))
    buffer.insert(temp + 1, i)
    pos = buffer.index(i)
print(buffer[buffer.index(2017) + 1])
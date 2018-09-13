def day6_b(input):
    history = []
    count = 0
    
    split_input = input.split()
    memory = list(map(int, split_input))
    size = len(memory)
    
    while(True):
        count += 1
        index = findMaxVal(memory)
        mem_size = memory[index]
        memory[index] = 0
        
        index = (index + 1) % size
        while(mem_size > 0):
            memory[index] += 1
            mem_size -= 1
            index = (index + 1) % size
            
    
        s = ''.join(str(n) for n in memory)
        if(s in history):
            temp_ind = history.index(s)+1
            return count - temp_ind
        history.append(s)
        
    

def findMaxVal(numbers):
    index = 0
    maxVal = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maxVal:
            index = i
            maxVal = numbers[i]
    return index

print(day6_b("14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"))

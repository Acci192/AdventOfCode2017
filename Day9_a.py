def day9_a(input):
    new_input = input
    while "!" in new_input:
        index = new_input.find("!")
        new_input = new_input[:index] + new_input[index+2:]
    
    while "<" in new_input:
        start = new_input.find("<")
        end = new_input.find(">")
        new_input = new_input[:start] + new_input[end + 1:]
    
    
    group = 0
    group_sum = 0
    
    for c in new_input:
        if c == "{":
            group += 1
            group_sum += group
        elif c == "}":
            group -= 1
    print(group_sum)

file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()
day9_a(input)
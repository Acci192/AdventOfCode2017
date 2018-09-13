def day15_a():
    A = 512
    B = 191
    
    counter = 0
    for i in range(40000000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647

        stringA = format(A, '032b')[16:]
        stringB = format(B, '032b')[16:]

        if stringA == stringB:
            counter += 1
            
    print(counter)
    

day15_a()
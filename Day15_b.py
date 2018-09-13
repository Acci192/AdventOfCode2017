
A = 512
B = 191

counter = 0
A_Val = []
B_Val = []
while True:
    if(len(A_Val) < 5000000):
        A = (A * 16807) % 2147483647
        if(int(A /4) == A/4):
            A_Val.append(format(A, '032b')[16:])
    
    if(len(B_Val) < 5000000):
        B = (B * 48271) % 2147483647
        if(int(B/8) == B/8):
            B_Val.append(format(B, '032b')[16:])
    
    
    if(len(A_Val) >= 5000000 and len(B_Val) >= 5000000):
        break

print("JUDGE")
      
for i in range(5000000):
    if(A_Val[i] == B_Val[i]):
        counter += 1
print(counter)
    



file_obj = open("input.txt", 'r')
input = file_obj.read()
file_obj.close()
def day11_a(input):
    ins = input.split(",")
    n = ins.count("n")
    ne = ins.count("ne")
    nw = ins.count("nw")
    s = ins.count("s")
    se = ins.count("se")
    sw = ins.count("sw")
    
    if n > s:
        n = n - s
        s = 0
    else:
        s = s - n
        n = 0
        
    if ne > sw:
        ne = ne - sw
        sw = 0
    else:
        sw = sw - ne
        ne = 0
        
    if nw > se:
        nw = nw - se
        se = 0
    else:
        se = se - nw
        nw = 0
    
    
    
    print(n)
    print(ne)
    print(nw)
    print(s)
    print(se)
    print(sw)
day11_a(input)
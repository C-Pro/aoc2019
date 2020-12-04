def get_params(mem, pos):
    a=mem[mem[pos+1]]
    b=mem[mem[pos+2]]
    c=mem[pos+3]
    return (a,b,c)

with open("input.txt", "rt") as f:
    mem = [int(x) for x in f.read().split(',')]
    mem[1] = 12
    mem[2] = 2
    pos=0
    while mem[pos]!=99:
        opcode=mem[pos]
        a,b,c = get_params(mem, pos)
        if opcode==1:
            mem[c]=a+b
        elif opcode==2:
            mem[c]=a*b
        else:
            raise ValueError(f"Bad opcode: {opcode}")
        pos+=4

    print(mem)

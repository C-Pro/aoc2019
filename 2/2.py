def get_params(mem, pos):
    a=mem[mem[pos+1]]
    b=mem[mem[pos+2]]
    c=mem[pos+3]
    return (a,b,c)

with open("input.txt", "rt") as f:
    memO = [int(x) for x in f.read().split(',')]

    for n in range(99):
        for v in range(99):
            mem = memO[:]
            mem[1] = n
            mem[2] = v
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

            if mem[0] == 19690720:
                print(100 * n + v)
                exit()
    print("oops")

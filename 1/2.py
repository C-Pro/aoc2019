def f(i):
    if i<6:
        return 0
    return i//3-2

assert(f(12)==2)
assert(f(14)==2)
assert(f(1969)==654)
assert(f(100756)==33583)

def f2(mass):
    amt=0
    while mass>0:
        amt+=mass
        mass=f(mass)
    return amt

assert(f2(f(12))==2)
assert(f2(f(1969))==966)
assert(f2(f(100756))==50346)

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    print(sum([f2(f(int(l))) for l in lines]))


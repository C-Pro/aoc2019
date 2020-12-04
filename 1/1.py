def f(i):
    if i<6:
        return 0
    return i//3-2

assert(f(12)==2)
assert(f(14)==2)
assert(f(1969)==654)
assert(f(100756)==33583)

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    print(sum([f(int(l)) for l in lines]))

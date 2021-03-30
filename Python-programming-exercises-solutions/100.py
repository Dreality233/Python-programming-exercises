def solve(heads,legs):
    ns = 'No solutions1'
    for i in range(heads+1):
        j = heads - i
        if 2*i+4*j == legs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)
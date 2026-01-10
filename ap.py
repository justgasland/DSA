def nthTermOfAP(a1, a2, n):
    nthTerm = a1
    d = a2 - a1
    for i in range(1, n):
        nthTerm += d
    return nthTerm

a1 = 2
a2 = 3
n = 4
print(nthTermOfAP(a1, a2, n))

def nthTermOfAP(a1, a2, n):
    return a1 + (n - 1) * (a2 - a1)
a1 = 2
a2 = 8
n = 4
print(nthTermOfAP(a1, a2, n))
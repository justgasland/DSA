def binomialcoeff(n,k):
    res=1
    if k>n-k:
        k=n-k
    for i in range(k):
        res=res*(n-i)
        res=res//(i+1)
    return res
def pascal(n):
    mat=[]
    for row in range(n):
        arr = []
        for i in range(row + 1):
            arr.append(binomialcoeff(row, i))
        mat.append(arr)
    return mat

n = 5
mat = pascal(n)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()
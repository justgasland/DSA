n = 4562
rev = 0

while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)


def reverse_number(n, revNum, basePos):
    if n > 0:
        reverse_number(n//10, revNum, basePos)
        revNum[0] += (n % 10) * basePos[0]
        basePos[0] *= 10

n = 4562
revNum = [0]  
basePos = [1]  
reverse_number(n, revNum, basePos)
print(revNum[0])
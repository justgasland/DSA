def findSum(n):
    sum =0
    i=1
    while i <= n:
        sum = sum + i
        i= i+1
    return sum

def find_Sum(n):
    if n==1:
        return 1
    return n + findSum(n-1)

if __name__ == "__main__":
    n = 293834  
    
    print(findSum(n))
    print(find_Sum(n))
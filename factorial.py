def factorial(n):
    ans =1
    i=1
    while (i <=n):
        ans = ans * i
        i= i+1
    return ans


# Recursive function to find factorial
def factoriall(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    num = 5
    print(factorial(num))
    print(factoriall(num))

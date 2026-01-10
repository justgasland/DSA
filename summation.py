def summation(n):
    return sum(i**2 for i in range(1, n + 1))

def summation_recursive(n):
    return n*(n + 1)*(2*n + 1)/6


if __name__ == "__main__":
    n = 2
    print(summation(n))
    n=456
    print(summation_recursive(n))
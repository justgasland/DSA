def sumOfDigits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum
def sumOFDigits():
    if n ==0:
        return 0
    return n % 10 + sumOfDigits(n // 10)
if __name__ == "__main__":
    n = 12345
    print(sumOfDigits(n))
    n = 12345
    print(sumOFDigits(n))


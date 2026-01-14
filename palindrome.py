def isPalindrome(n):
    reverse = 0
    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    
    return (reverse == abs(n))

if __name__ == "__main__":
    
    n = 12321
    if isPalindrome(n) == True:
        print("True")
    else:
        print("False")

def isPalindrome(n):

    # Convert the absolute value
    # of number to string
    s = str(abs(n))
    length = len(s)

    for i in range(length // 2):

        # Comparing i th character from starting
        #  and len-i th character from end
        if s[i] != s[length - i - 1]:
            return False
    return True
    
if __name__ == "__main__":
    n = 12321
    if isPalindrome(n) == True:
        print("True")
    else:
        print("False")
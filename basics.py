#  Basic to check for even numbers
def is_even(n):
    if (n & 1 )==0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    n = 15
    if is_even(n):
        print("true")
    else:
        print("false")

# Multiplication
 
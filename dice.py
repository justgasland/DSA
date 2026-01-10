def oppositeFaceOfDice(n):
    if n == 1:
        return 6
    elif n == 2:
        return 5
    elif n == 3:
        return 4
    elif n == 4:
        return 3
    elif n == 5:
        return 2
    else:
        return 1

n = 2
print(oppositeFaceOfDice(n))

def oppositeFaceOfDice(n):
    
    # Stores number on opposite face
    # of dice
    ans = 7 - n
    return ans

n = 2
print(oppositeFaceOfDice(n))
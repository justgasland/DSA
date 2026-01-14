def pair(n):
    count = 0
    for a in range(1, n +1):
        for b in range( n +1):
            if a**3 + b**3 == (a + b)**3:
                count += 1
    return count
n = 9
print(pair(n))


import math 

def countPairs(n):
    count = 0
    
    # Check for each number 1 to cbrt(n)
    for i in range(1, int(math.pow(n, 1/3)) + 1):
        # Store cube of a number
        cb = i * i * i
        
        # Subtract the cube from given n
        diff = n - cb
        
        # Check if the difference is also a perfect cube
        cbrt_diff = round(diff ** (1/3))
        
        # If yes, then increment count
        if cbrt_diff * cbrt_diff * cbrt_diff == diff:
            count += 1

    return count

if __name__ == "__main__":
  n = 2
  print(countPairs(n))
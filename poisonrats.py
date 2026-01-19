
import math
def minRats(n):
    return math.ceil(math.log2(n))
n = 1025; 
print("Minimum ", end = "")
print(minRats(n), end = " ")
print("rat(s) are required")
n=1234567589333862
if int(n)%4==0:
  print("Yes") 
else: 
  print("No")

def check(st):
    n = len(st)

    if n == 0:
        return False

    if n == 1:
        return (int(st[0]) % 4 == 0)
    last = int(st[n - 1])
    second_last = int(st[n - 2])

    return ((second_last * 10 + last) % 4 == 0)

st = "76952"

if check(st):
    print("Yes")
else:
    print("No")

def check(s):
    # Empty string
    if len(s) == 0:
        return False
    # If there is single digit
    if len(s) == 1:
        return int(s) % 4 == 0
    # If number formed by last two digits is divisible by 4.
    return int(s[-2:]) % 4 == 0

s = "76953"

# Function call
print("Yes" if check(s) else "No ")
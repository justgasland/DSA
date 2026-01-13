#  code to check the validity of a triangle given the lengths of its three sides
def checkValidity(a, b, c): 
    
    # check condition 
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True        

# driver code 
a = 7
b = 2   
c = 5
if checkValidity(a, b, c):
    print("Valid") 
else:
    print("Invalid")
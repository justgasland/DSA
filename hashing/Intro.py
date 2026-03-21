# Hashing is a techniqe where by input is passed through a function to give a fixed size  output
# The output is called hash value or digest
# hash values are stored in a storage system called hash table
# Hashing is used in data structures like hash maps, hash sets, and hash tables
# Hashing is used in cryptography to create digital signatures and to store passwords securely

# key features of hashing:
# fixed output
# efficency
# unifomm distribution
# collision resistance


# HASH FUNCTION
# multipication
# division
# cryptographic hash functions like SHA-256, MD5, etc.
# folding
# mid square


def isSubset(a, b):
    m, n = len(a), len(b)

    for i in range(n):
        found = False
        for j in range(m):
            if b[i] == a[j]:
                found = True
                # mark as visited
                a[j] = -1  
                break
            
        # If any element is not found, return false    
        if not found:
            return False
    
    # If all elements are found, return true
    return True


if __name__ == '__main__':
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 7, 1]

    if isSubset(a, b):
        print("true")
    else:
        print("false")


def areDisjoint(a, b):
    
    # Sorting both the arrays
    a.sort()
    b.sort()
    
    # Initializing pointers at the  
    # beginning of both the arrays
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
        
        # If any common element is found, then
        # given arrays are not disjoint
        if a[i] == b[j]:
            return False
            
        # Incrementing the pointer  
        # having smaller value
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    
    return True

# Custom Input
a = [12, 34, 11, 9, 3]
b = [7, 2, 1, 5]

if areDisjoint(a, b):
    print("True")
else:
    print("False")
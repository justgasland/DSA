def findDuplicate(arr):

    # Sort the array
    arr.sort()

    for i in range(len(arr) - 1):

        # If the adjacent elements are equal
        if arr[i] == arr[i + 1]:
            return arr[i]
    return -1



def findDuplicate(arr):
    
    # Create a set
    s = set()
    for x in arr:

        # If the element is already in the set
        if x in s:
            return x
        s.add(x)
    return -1

def findDuplicate(arr):
    n = len(arr)
  
    # Find the sum of elements in the array
    # and subtract the sum of the first n-1 
    # natural numbers to find the repeating element.
    totalSum = sum(arr)
    duplicate = totalSum - ((n - 1) * n // 2)
    return duplicate


if __name__ == "__main__":
    arr = [1, 3, 2, 3, 4]
    print(findDuplicate(arr))
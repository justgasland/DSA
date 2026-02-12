def array_distance(arr, k):
    n=len(arr)

    for i in range(0, len(arr)):
        
        for j in range(1, k+1):
            c=i+j
            if c < n and arr[i] == arr[c]:
                return True
    return False
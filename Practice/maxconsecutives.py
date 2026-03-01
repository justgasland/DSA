def maxOnes(arr, k):
    res = 0
    
    # Exploring all subarrays
    for i in range(len(arr)):
        
        # Counter for zeroes
        cnt = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                cnt += 1
            
            # If cnt is less than or equal to k, then  
            # all zeroes can be flipped to one
            if cnt <= k:
                res = max(res, j - i + 1)
    
    return res

if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    print(maxOnes(arr, k))
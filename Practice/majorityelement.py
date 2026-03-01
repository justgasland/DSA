# class Solution:
#     def majorityElement(self, arr):
#         #code here
#         n = len(arr)
#         num= n//2
        
#         for i in range(0, n):
#             count=0
#             can=arr[i]
#             if arr[i] == can:
#                 count+=1
#             if count > num:
#                 return arr[i]
#         return -1

def majorityElement(self, arr):
    n = len(arr)
    num = n // 2
    counts = {}
    
    for element in arr:
        if element in counts:
            counts[element] = counts[element] + 1
        else:
            counts[element] = 1  
        
        if counts[element] > num:
            return element
    
    return -1
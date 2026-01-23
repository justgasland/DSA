#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        left=0
        add=0
        for i in range(0, len(arr)):
            add +=arr[i]
            
            while add> target:
                add-=arr[left]
                left +=1 
                
            if add == target:
                return [left+1 , i +1]
        return [-1]
                
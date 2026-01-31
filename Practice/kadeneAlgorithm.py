class Solution:
    def maxSubarraySum(self, arr):
        max_sum = float('-inf')
        for i in range(0, len(arr)):
    
            for j in range(i, len(arr)):
                sum =0
                for k in range(i, j + 1):
                    sum += arr[k]
                max_sum = max(max_sum, sum)
        return max_sum
    
class Solution:
    def maxSubarraySum(self, arr):
        max_sum = float('-inf') 
        current_sum = 0
        for i in range(0, len(arr)):
            current_sum += arr[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0 
        return max_sum

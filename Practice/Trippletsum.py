class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n=len(arr)
        
        
        for left in range(0,n-2):
            mid= left + 1
            right = n-1
            while mid < right:
                sum = arr[left] + arr[mid] + arr[right]
                if sum == target:
                    return True
                elif sum < target:
                    mid += 1
                else:
                    right -= 1
        return False

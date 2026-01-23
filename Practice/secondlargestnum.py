class Solution:
    def getSecondLargest(self, arr):
        largest = 0
        second_largest = 0
        
        for num in arr:
            if num > largest:
                second_largest = largest
                
                largest = num
            elif num > second_largest and num != largest:
                
                second_largest = num

        if second_largest == 0:
            return -1

        return second_largest
    
if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    obj = Solution()
    print(obj.getSecondLargest(arr))
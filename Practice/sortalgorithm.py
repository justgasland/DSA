class Solution:
    def sort(self, arr):
        sorted=[]
        n=len(arr)
        for i in range(0, n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    

class Solution:
    def sort012(self, arr):
        
        count0 = 0
        count1 = 0
        count2 = 0
        
        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:  
                count2 += 1
        

        index = 0
        
  
        for i in range(count0):
            arr[index] = 0
            index += 1
        
        
        for i in range(count1):
            arr[index] = 1
            index += 1
        
        
        for i in range(count2):
            arr[index] = 2
            index += 1
        
        return arr


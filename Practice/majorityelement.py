class Solution:
    def majorityElement(self, arr):
        #code here
        n = len(arr)
        num=0
        for i in range(0, n):
            count=0
           
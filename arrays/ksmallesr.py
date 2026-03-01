class Solution:
    def kthSmallest(self, arr, k):
        # Sort the array
        sorted_arr = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    sorted_arr.append(arr[i])
                else:
                    sorted_arr.append(arr[j])
        
        # Return the k-1 indexed element
        return sorted_arr [k - 1]
class Solution:
    def segregateEvenOdd(self, arr):
        even = []
        odd = []

        for i in arr:
            if (i & 1) == 0:
                even.append(i)
            else:
                odd.append(i)

        even.sort()
        odd.sort()

        # Modify arr in-place
        for i in range(len(even)):
            arr[i] = even[i]
        for i in range(len(odd)):
            arr[len(even) + i] = odd[i]

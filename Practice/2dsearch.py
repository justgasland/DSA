class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x):
        for row in matrix:
            if x in row:
                return 1
            else:
                return 0
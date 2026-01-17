class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x):
        for row in matrix:
            if x in row:
                return 1
            else:
                return 0

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x):
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == x:
                    return 1
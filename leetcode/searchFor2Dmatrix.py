__author__ = 'Lily'

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix is None:
            return False
        m=len(matrix[0])
        n=len(matrix)
        for i in range(0,n):
            if target<matrix[i][m-1]:
                row=i
                for j in range(0,m):
                    if target==matrix[i][j]:
                        return True
                return False
            elif target==matrix[i][m-1]:
                return True
        return False

solution=Solution()
print solution.searchMatrix([[1,3,5]],3)
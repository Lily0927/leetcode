__author__ = 'Lily'

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        if matrix==None:
            return
        n=len(matrix)
        for i in range(0,n/2):
            for j in range (0,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[n-1-i][j]
                matrix[n-1-i][j]=temp
        for i in range(0,n):
            for j in range(i,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
__author__ = 'Lily'


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row = False
        column = False
        m = len(matrix[0])
        n = len(matrix)
        for i in range(0, m):
            if matrix[0][i] == 0:
                row = True
                break
        for j in range(0, n):
            if matrix[j][0] == 0:
                column = True
                break
        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(0, m):
            if matrix[0][i] == 0:
                for j in range(0, n):
                    matrix[j][i] = 0
        for i in range(0, n):
            if matrix[i][0] == 0:
                for j in range(0, m):
                    matrix[i][j] = 0
        if row == True:
            for i in range(0, m):
                matrix[0][i] = 0
        if column == True:
            for i in range(0, n):
                matrix[i][0] = 0




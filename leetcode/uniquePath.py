__author__ = 'Lily'

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        grid=[[0 for x in range(0,100)]for x in range(0,100)]
        if m==0 and n==0:
            return 0
        for i in range(0,m):
        	grid[i][0]=1

        for j in range(0,n):
        	grid[0][j]=1

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]
        return grid[m-1][n-1]

solution=Solution()
print solution.uniquePaths(2,2)
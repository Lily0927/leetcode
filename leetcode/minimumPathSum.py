__author__ = 'Lily'


class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]

        for j in range(1, m):
            grid[j][0] = grid[j - 1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i - 1][j] <= grid[i][j - 1]:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]

                else:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]

        return grid[grid.length - 1][grid[0].length - 1]

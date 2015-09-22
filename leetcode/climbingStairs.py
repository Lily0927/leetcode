__author__ = 'Lily'


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        res=[0]*(n+1)
        res[0]=1
        res[1]=1
        for i in range(2,n+1):
            res[i]=res[i-1]+res[i-2]
        return res[n]
solution=Solution()
print solution.climbStairs(3)
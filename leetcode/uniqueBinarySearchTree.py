__author__ = 'Lily'

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        result=[0]*(n+1)
        if n==0:
            return 1
        if n==1:
            return 1
        result[0]=1
        result[1]=1

        for i in range (2,n+1):
            for k in range(0,i):
                result[i]+=result[k]*result[i-1-k]
        return result[n]

solution=Solution()
print solution.numTrees(3)
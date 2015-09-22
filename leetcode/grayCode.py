__author__ = 'Lily'

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n==None:
            return 0
        result=[0]
        for i in range(n):
            temp=1<<i
            for j in range(len(result)-1,-1,-1):
                result.append(temp+result[j])
        return result

solution=Solution()
print solution.grayCode(2)
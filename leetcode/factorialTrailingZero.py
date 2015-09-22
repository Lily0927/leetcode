__author__ = 'Lily'

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        while n>0:
            sum+=n/5
            n=n/5
        return sum

solution=Solution()
print solution.trailingZeroes(30)
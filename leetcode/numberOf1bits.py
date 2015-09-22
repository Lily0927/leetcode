__author__ = 'Lily'

class Solution:
    # @param n, an integer
    # @return an integer
    @staticmethod
    def hammingWeight(n):
        count=0
        while(n):
            if n%2==1:
                count=count+1
            n=n/2
        if n<0:
            count=count+1
        return count
# solution=Solution()
print Solution.hammingWeight(-2147483648)
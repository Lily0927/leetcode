__author__ = 'Lily'

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        temp=32
        if n ==0:
            return 0
        while temp>0:
            result=result<<1
            if n&1==1:
               result=result+1
            n=n>>1
            temp-=1
            print result
        print type(result)
        return result

solution=Solution()
print solution.reverseBits(-1)
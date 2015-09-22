__author__ = 'Lily'

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        store={}
        while 1:
            temp=self.square(n)
            if temp==1:
                return True
            elif temp in store:
                return False
            store[temp]=0
            n=temp
        return True


    def square(self,n):
        sum=0
        for i in str(n):
            sum+=int(i)*int(i)
        return sum

solution=Solution()
print solution.isHappy(19)
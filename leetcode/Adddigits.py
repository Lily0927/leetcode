__author__ = 'Lily'

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num/10==0:
            return num
        list_of_ints=[int(i) for i in str(num)]
        sum=0
        for i in list_of_ints:
            sum+=i
        return self.addDigits(sum)

solution=Solution()
print solution.addDigits(38)
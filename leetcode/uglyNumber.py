__author__ = 'Lily'

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>=2:
            if num%2==0:
                num/=2
            elif num%3==0:
                num/=3
            elif num%5==0:
                num/=5
            else:
                return False
        return True

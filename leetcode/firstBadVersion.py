__author__ = 'Lily'

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        test=(n+0)/2
        start=1
        end=n
        while test>0:
            if isBadVersion(test) is True:
                if isBadVersion(test-1) is False:
                    return test
                else:
                    test=(start+test)/2
            else:
                if isBadVersion(test+1) is True:
                    return test+1
                else:
                    test=(test+end)/2
        return test

    def firstBadVersion(self,n):
        if n==0:
            return 0
        l=1
        while l<=n:
            mid=l+(n-l)/2
            if isBadVersion(mid) is True:
                n=mid-1
            else:
                l=mid+1
        return l




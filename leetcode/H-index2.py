__author__ = 'Lily'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n=len(citations)
        l=0
        temp=0
        if n==0:
            return 0
        e=n-1
        while l<=e:
            mid=l+(e-l)/2
            if citations[mid]==n-mid:
                return n-mid
            elif citations[mid]>n-mid:
                e=mid-1
                temp=n-mid
            else:
                l=mid+1
        return temp

solution=Solution()
print solution.hIndex([1,1,1,1,1])
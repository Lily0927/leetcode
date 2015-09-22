__author__ = 'Lily'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        length=len(citations)
        for i in range(0,length):
            if citations[i]>=length-i:
                return length-i
        return 0

solution=Solution()
print solution.hIndex([100])
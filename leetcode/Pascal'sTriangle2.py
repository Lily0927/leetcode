__author__ = 'Lily'

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        for i in range(1, rowIndex+1):
            row=[1]+[row[x]+row[x-1] for x in range(1,i)]+[1]
        return row
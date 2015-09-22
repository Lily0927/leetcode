__author__ = 'Lily'

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result={}
        for i in nums:
            if i in result:
                del result[i]
            else:
                result[i]=1
        array=[x for x in result]
        return array

solution=Solution()
print solution.singleNumber([1,2,1,2,3,5])
__author__ = 'Lily'

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum=(0+n)*(n+1)/2
        sum2=0
        for i in nums:
            sum2+=i
        return sum-sum2


solution=Solution()
print solution.missingNumber([1])
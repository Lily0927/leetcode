__author__ = 'Lily'

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        result=[0]*len(nums)
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            result[0]=nums[0]
            result[1]=max(nums[0],nums[1])
            for i in range (2,len(nums)):
                result[i]=max(nums[i]+result[i-2],result[i-1])
        return result[len(nums)-1]

solution=Solution()
print solution.rob([1,1,1])
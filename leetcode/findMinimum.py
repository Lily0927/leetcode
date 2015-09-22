__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if nums==None:
            return None
        if len(nums)!=1:
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    return nums[i]
        return nums[0]
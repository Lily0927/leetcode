__author__ = 'Lily'

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if nums is None:
            return None
        max=0
        index=0
        for i in range(0,len(nums)):
            if nums[i]>max:
                max=nums[i]
                index=i
        return index
__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if nums==None:
            return 0
        for i in range (0, len(nums)):
            if nums[i]>=target:
                return i
        return 0
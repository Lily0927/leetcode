__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        max=nums[0]
        current=0
        for i in nums:
            current+=i
            if current>=max:
                max=current
            if current<0:
                current=0
        return max
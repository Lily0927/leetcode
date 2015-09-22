__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        result=[1]*len(nums)
        temp1=[0]
        left=1
        for i in range(0,len(nums)-1):
            left*=nums[i]
            result[i+1]*=left
        right=1
        for i in range(len(nums)-1,0,-1):
            right*=nums[i]
            result[i-1]*=right
        return result

__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        j=0
        for i in range(0,len(nums)):
            if nums[j]!=val:
                nums[j]=nums[i]
                j+=1
        return j

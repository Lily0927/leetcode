__author__ = 'Lily'

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        index=0
        for i in nums:
            if i !=0:
                nums[index]=i
                index+=1
        while index<length:
            nums[index]=0
            index+=1
        return nums

solution=Solution()
print solution.moveZeroes([0,0,0,0])
__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if nums==None:
            return None
        index0=0
        index1=0
        index2=0
        for i in nums:
            if i==0:
                index0+=1
            elif i==1:
                index1+=1
            else:
                index2+=1
        for i in range(index0):
            nums[i]=0
        for i in range(index0,index0+index1):
            nums[i]=1
        for i in range(index0+index1,index0+index1+index2):
            nums[i]=2
        return nums

solution=Solution()
print solution.sortColors([0])

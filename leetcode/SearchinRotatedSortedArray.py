__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
        return -1

    def search2(self,nums,target):
        if nums is None:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        start=0
        end=len(nums)-1
        middle=0
        while(start<=end):
            middle=start+(end-start)/2
            if nums[middle]==target:
                return middle
            if nums[middle]<nums[end]:
                if nums[middle]<target and target<=nums[end]:
                    start=middle+1
                else:
                    end=middle-1
            elif nums[middle]<nums[end]:
                if nums[start]<=target and target<nums[middle]:
                    end=middle-1
                else:
                    start=middle+1
            else:
                start+=1
        return -1
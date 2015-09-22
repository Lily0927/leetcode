__author__ = 'Lily'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        result={}
        for i in nums:
            if i in result:
                result[i]=result[i]+1
                if result[i]>len(nums)/2:
                    return i
            else:
                result[i]=1
                if 1>len(nums)/2:
                    return i
        return 0
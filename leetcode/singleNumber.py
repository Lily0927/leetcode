__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        if nums==None:
            return None
        result={}
        for i in nums:
            if i in result:
                result[i]+=1
            else:
                result[i]=1

        for j in result:
            if result[j]<3:
                return j
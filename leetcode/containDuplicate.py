__author__ = 'Lily'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums==None:
            return False
        s=set([])
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
__author__ = 'Lily'

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=map(str,nums)
        nums.sort(cmp=lambda x,y:cmp(x+y,y+x),reverse=True)
        print nums
        return ''.join(nums)


solution=Solution()
print solution.largestNumber([3,34,5])
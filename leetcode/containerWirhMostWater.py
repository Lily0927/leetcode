__author__ = 'Lily'

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if height is None:
            return 0
        start=0
        maxR=0
        end=len(height)-1
        while start<end:
            maxR=max(maxR,(end-start)*min(height[start],height[end]))
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return maxR
__author__ = 'Lily'

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        min=0
        result=0
        for i in prices:
            if i<min:
                min=i
            else:
                result=max(i-min,result)
        return result
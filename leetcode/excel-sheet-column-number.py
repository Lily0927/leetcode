__author__ = 'Lily'
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        result=0
        for i in s:
            result=result*26+ord(i)-ord('A')+1
        return result

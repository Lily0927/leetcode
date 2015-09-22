__author__ = 'Lily'


class Solution:
    # @param {integer} n
    # @return {string[]}
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        self.dfs(n, n, "")
        # print self.result
        for i in self.result:
            print i


    def dfs(self, left, right, string):
        if left>right:
            return
        if left == 0 and right == 0:
            self.result.append(string)
            # print "in dfs",string
            return
        if left > 0:
            self.dfs(left - 1, right, string + "(")
        if right > 0:
            self.dfs(left, right - 1, string + ")")



solution = Solution()
solution.generateParenthesis(1)


__author__ = 'Lily'

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def __init__(self):
        self.result=0
    def kthSmallest(self, root, k):
        num=0
        self.visit(root,k,num)
        return self.result


    def visit(self,root,k,num):
        if root is None:
            return
        self.visit(root.left,k,num)
        if num<k:
            num+=1
            if num==k:
                self.result=root.val
                return
        self.visit(root.right,k,num)


__author__ = 'Lily'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if root==None:
            return 0
        if self.height(root)==-1:
            return False
        return True
    def height(self,root):
        if root==None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        if left==-1 or right==-1:
            return -1
        if right-left>1 or left-right>1:
            return -1
        return max(left,right)+1

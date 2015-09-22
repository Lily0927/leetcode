__author__ = 'Lily'

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left!=None and root.right!=None:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        if root.left!=None:
            return 1+self.minDepth(root.left)
        if root.right!=None:
            return 1+self.minDepth(root.right)
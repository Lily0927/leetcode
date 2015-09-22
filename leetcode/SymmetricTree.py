__author__ = 'Lily'

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.symmetric(root.left,root.right)


    def symmetric(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return self.symmetric(p.left,q.right) and self.symmetric(p.right,q.left) and p.val==q.val
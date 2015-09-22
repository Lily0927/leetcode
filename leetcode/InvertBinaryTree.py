__author__ = 'Lily'
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if(root==None):
            return None
        temp=root.left
        root.left=root.right
        root.right=temp

        if root.left!=None:
            self.invertTree(root.left)
        if root.right!=None:
            self.invertTree(root.right)
        return root
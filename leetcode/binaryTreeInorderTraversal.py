__author__ = 'Lily'
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        l=[]
        result=[]
        if root==None:
            return result
        l.append(root)
        while l:
            temp=l.pop()
            if temp==None:
                continue
            if isinstance(temp,int):
                result.append(temp)
            else:
                l.append(temp.right)
                l.append(temp.val)
                l.append(temp.left)
        return result


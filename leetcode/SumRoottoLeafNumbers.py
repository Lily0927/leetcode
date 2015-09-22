__author__ = 'Lily'

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        sum=0
        path=0
        self.generate(root,sum,path)
        return sum

    def generate(self,root,sum,path):
        if root is None:
            return
        path=path*10+root.val
        if root.left is None and root.right is None:
            sum+=path
            return
        self.generate(root.left,sum,path)
        self.generate(root.right,sum,path)

solution=Solution()
print solution.sumNumbers([9])
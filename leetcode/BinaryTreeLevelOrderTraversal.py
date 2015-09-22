__author__ = 'Lily'

class Solution(object):

    def levelOrder(self, root):
        from collections import deque
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        if root is None:
            return result
        queue=deque(root)
        while queue != None:
            print queue
            layer=[]
            for i in range(0,len(queue)):
                head=queue.popleft()
                layer.append(head.val)
                if head.left!=None:
                    queue.append(head.left)
                if head.right!=None:
                    queue.append(head.right)
                result.append(layer)
        return result





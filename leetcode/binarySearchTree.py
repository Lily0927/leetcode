__author__ = 'Lily'


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack=[]
        self.pushleft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        top=self.stack.pop()
        self.pushleft(top.right)
        return top.val

    def pushleft(self,root):
        while root:
            self.stack.append(root)
            root=root.left
__author__ = 'Lily'

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root==None:
            return
        row=root
        while row.left!=None:
            col=row
            while col!=None:
                col.left.next=col.right
                if col.next!=None:
                    col.right.next=col.next.left
                col=col.next
            row=row.left

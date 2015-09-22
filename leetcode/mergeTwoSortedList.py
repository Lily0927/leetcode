__author__ = 'Lily'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1==None and l2==None:
            return None
        result=ListNode(0)
        temp=result
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                result.next=l1
                l1=l1.next
            else:
                result.next=l2
                l2=l2.next
        if l1==None:
            result.next=l2
        elif l2==None:
            result.next=l1

        return temp.next

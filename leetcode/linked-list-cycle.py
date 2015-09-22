__author__ = 'Lily'

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head.next==None:
            return False
        slow=head
        fast=head
        while fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

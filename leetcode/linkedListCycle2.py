__author__ = 'Lily'


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        slow=head
        fast=head
        while slow !=None and fast!=None:
            slow=slow.next
            fast=fast.next
            if fast!=None:
                fast=fast.next
            if slow== fast:
                break
        if fast is None:
            return None
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next

        return fast
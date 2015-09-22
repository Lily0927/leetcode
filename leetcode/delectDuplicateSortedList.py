__author__ = 'Lily'

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        result=head
        while head.next!=None:
            if head.val==head.next.val:
                if head.next.next!=None:
                    head.next=head.next.next
                else:
                    head.next=None
            else:
                head=head.next
        return result

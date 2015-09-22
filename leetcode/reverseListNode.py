__author__ = 'Lily'

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head.next==None:
            return head
        var=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return var
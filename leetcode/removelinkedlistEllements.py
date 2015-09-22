__author__ = 'Lily'

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp=head
        if temp is None:
            return None
        record=None
        while(temp.next!=None):
            if temp.val==val:
                temp.val=temp.next.val
                temp.next=temp.next.next
            else:
                record=temp
                temp=temp.next
        if temp.val==val:
            if record is None:
                return None
            record.next=None

        return head
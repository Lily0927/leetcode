__author__ = 'Lily'

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        dic1={}
        n=0
        while headA.next!=None:
            dic1[headA]=n
            n+=1
            headA=headA.next
        while headB.next!=None:
            if headB in dic1:
                return headB
            else:
                headB=headB.next
        return None
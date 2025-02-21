class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prevGroupEnd = dummy
        
        while True:
            kthNode = self.getKthNode(prevGroupEnd, k)
            if not kthNode:
                break
            
            nextGroupStart = kthNode.next
            
            prev, curr = kthNode.next, prevGroupEnd.next
            while curr != nextGroupStart:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroupEnd.next
            prevGroupEnd.next = kthNode
            prevGroupEnd = temp
        
        return dummy.next

    def getKthNode(self, start: ListNode, k: int) -> ListNode:
        while start and k > 0:
            start = start.next
            k -= 1
        return start

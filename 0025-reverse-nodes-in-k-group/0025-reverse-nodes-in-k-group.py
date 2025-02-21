class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev_n = dummy
        
        while True:
            kthNode = self.getKthNode(prev_n, k)
            if not kthNode:
                break
            
            start_n = kthNode.next
            
            prev, curr = kthNode.next, prev_n.next
            while curr != start_n:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_n.next
            prev_n.next = kthNode
            prev_n = temp
        
        return dummy.next

    def getKthNode(self, start: ListNode, k: int) -> ListNode:
        while start and k > 0:
            start = start.next
            k -= 1
        return start

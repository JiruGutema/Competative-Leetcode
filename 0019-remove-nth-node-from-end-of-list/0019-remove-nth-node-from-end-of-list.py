# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        dummy = ListNode(0)  
        dummy.next = head
        
        count = 0
        left = dummy
        right = head

        while right:
            if count >= n:
                left = left.next
            right = right.next
            count += 1

        left.next = left.next.next
        
        return dummy.next

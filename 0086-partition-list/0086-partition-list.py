# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right = ListNode(),ListNode()
        taill,tailr = left,right
        while head:
            if head.val < x:
                taill.next = head
                taill = taill.next
            else:
                tailr.next = head
                tailr =tailr.next
            head = head.next
        taill.next = right.next
        tailr.next = None
        return left.next
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        values = []

  
        while current:
            values.append(current.val)
            current = current.next

        current = head
        values = values[::-1]
        for i in range(len(values)):
            current.val = values[i]
            current = current.next

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # Create a set of values in the nums list for faster lookup
        nums_set = set(nums)
        
        # Create a dummy node to simplify the logic
        dummy = ListNode(0)
        dummy.next = head
        
        # Remove nodes from the linked list
        prev, curr = dummy, head
        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True

        temp = []

        current = head
        while current:
            temp.append((current.val))
            current = current.next
        
        return temp == temp[::-1]
        


       
        # node = head
        # n = 0
        # while node:
        #     n += 1
        #     node = node.next

        # node1 = head
        # for i in range(n // 2):
     
        #     j = n
        #     h = 0
        #     temp = head
        #     while temp and h < j - i - 1:
        #         temp = temp.next
        #         h += 1

           
        #     if node1.val != temp.val:
        #         return False

        #     node1 = node1.next

        # return True


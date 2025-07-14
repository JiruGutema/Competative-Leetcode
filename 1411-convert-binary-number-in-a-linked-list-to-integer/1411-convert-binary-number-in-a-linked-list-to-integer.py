# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        num = 0
        node = head

        while node:
            nums.append(node.val)
            node = node.next
       
        for i in range(len(nums)):
            
            conv = (2**i)*nums[::-1][i]
           
            num = num + conv
        return num
        # pointer = 0
        # itr = 0
        # num = 
        
        # current = node
        # while current:
        #     itr += 1
        #     current = current.next
        # pointer = itr
        

        # for i in range(itr):
        #     node = head
        #     while itr < pointer - i:
        #         node = node.next
            
        #     num = 

        
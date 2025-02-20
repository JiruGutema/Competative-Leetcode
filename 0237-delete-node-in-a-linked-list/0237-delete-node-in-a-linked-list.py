# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        curr = node
        currNxt = curr.next
        while currNxt:
            curr.val = currNxt.val
            prev = curr
            curr = currNxt
            currNxt = curr.next

        prev.next = None
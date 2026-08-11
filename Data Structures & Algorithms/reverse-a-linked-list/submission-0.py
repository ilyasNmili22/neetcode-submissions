# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        current_Node = head
        prev = None
        while(current_Node):
            tmp = current_Node.next
            current_Node.next = prev
            prev = current_Node
            current_Node = tmp
        return prev

        
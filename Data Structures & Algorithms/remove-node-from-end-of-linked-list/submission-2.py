# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        moves = 0
        curr = head
        while(curr):
            moves += 1
            curr = curr.next
        moves -= (n + 1)

        curr = head
        if moves < 0:
            head = head.next
            return head
        if moves == 0:
            head.next = head.next.next
            return head
        while(moves > 0):
            curr = curr.next
            moves -= 1
        curr.next = curr.next.next
        return head
class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		slow = fast = head
		while (fast and fast.next):
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False

'''
How It Works
Two Pointers:

A slow pointer moves one step at a time.
A fast pointer moves two steps at a time.
Purpose:

If there’s a cycle in the data structure, the fast pointer will eventually meet the slow pointer.
If there’s no cycle, the fast pointer will reach the end of the data structure first.
This difference in speed is key to detecting patterns efficiently.
'''
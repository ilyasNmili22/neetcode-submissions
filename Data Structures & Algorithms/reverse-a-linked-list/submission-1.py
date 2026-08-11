class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		current = head
		previous = None
		while (current):
			tmp = current.next
			current.next = previous
			previous = current
			current = tmp
			
		return previous
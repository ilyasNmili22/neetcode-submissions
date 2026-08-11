class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		size = 0
		current = head
		while(current):
			size += 1
			current = current.next
		if size == n == 1:
			return None
		if n == size:
			return head.next
		last = size - n
		current = head
		for i in range(last - 1):
			current = current.next
		current.next = current.next.next
		return head
	
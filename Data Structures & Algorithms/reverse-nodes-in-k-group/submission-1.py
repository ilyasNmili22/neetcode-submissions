class Solution:
	def reverseList(self, head: Optional[ListNode], n) -> Optional[ListNode]:
		current = head
		previous = None
		k = 0
		while (current and k < n):
			tmp = current.next
			current.next = previous
			previous = current
			current = tmp
			k += 1
		head.next = current
		#return last one
		return head
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		size = 0
		first = curr = head
		while(curr):
			size += 1
			if size == k:
				tmp = curr.next
				ret = curr
				last = self.reverseList(head, k)
				curr = tmp
			elif size % k == 0:
				tmp = curr.next
				rev = self.reverseList(last.next, k)
				last.next = curr
				last = rev
				curr = tmp			
			else:
				curr = curr.next
		
		return ret

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        current = head 
        while(current):
            if current not in my_set:
                my_set.add(current)
            else:
                 return True
            current = current.next
        return False
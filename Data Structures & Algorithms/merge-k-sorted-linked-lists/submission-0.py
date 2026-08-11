# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Not a good solution cause I ceate a new lists
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_lists = []
        for i in range(len(lists)):
              curr = lists[i]
              while(curr):
                    all_lists.append(curr.val)
                    curr = curr.next
        all_lists.sort()
        ret = ListNode()
        curr = ret
        for i in range(len(all_lists)):
                curr.next = ListNode(all_lists[i])
                curr = curr.next
        return ret.next
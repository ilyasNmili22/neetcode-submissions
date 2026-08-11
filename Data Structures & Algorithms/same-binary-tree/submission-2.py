# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val != q.val:
            return False
        s1, s2 = [p], [q]
        while (s1 and s2):
            node1 = s1.pop()
            node2 = s2.pop()
            if not node1 and not node2: continue
            elif node1 and node2 and node1.val == node2.val:
                s1.append(node1.right)
                s2.append(node2.right)
                s1.append(node1.left)
                s2.append(node2.left)
            else:
                return False
        return not s1 and not s2
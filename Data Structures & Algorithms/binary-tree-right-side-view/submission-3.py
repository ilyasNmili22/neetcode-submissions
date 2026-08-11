# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ret = []
        q = deque()
        q.append(root)
        while(q):
            x = len(q)
            ret.append([])
            for i in range(x):
                node = q.popleft()
                ret[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return [x[-1] for x in ret]
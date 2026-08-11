# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        def dfs(root, k):
            if not root: return
            dfs(root.left, k)
            if len(ret) >= k: return
            ret.append(root.val)
            dfs(root.right, k)
        dfs(root, k)
        print(ret)
        return ret[-1]
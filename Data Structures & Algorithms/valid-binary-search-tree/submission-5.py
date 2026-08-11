# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def mx(root):
            if not root: 
                return -float('inf')
            left_mx = mx(root.left)
            right_mx = mx(root.right)
            return max(root.val, left_mx, right_mx)
        def mn(root):
            if not root: 
                return float('inf')
            left_mn = mn(root.left)
            right_mn = mn(root.right)
            return min(root.val, left_mn, right_mn)
        
        if not root: return True
        if not (mx(root.left) < root.val < mn(root.right)): return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        
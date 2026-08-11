class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_pos_val, max_pos_val):
            if not root:
                return True
            if not (min_pos_val < root.val < max_pos_val):
                return False
            return dfs(root.left, min_pos_val, root.val) and dfs(root.right,root.val, max_pos_val)
        return dfs(root, -2 ** 31 - 1, 2 ** 31)
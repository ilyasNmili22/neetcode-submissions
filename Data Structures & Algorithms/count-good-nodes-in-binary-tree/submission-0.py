"""The nonlocal keyword is used to modify a variable in 
an enclosing (but not global) scope.This is useful in nested 
functions where you want to modify a variable from an outer function."""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, vmax):
            nonlocal count
            if not root:
                return
            if root.val >= vmax:
                count += 1
                vmax = root.val
            dfs(root.left, vmax)
            dfs(root.right, vmax)
        dfs(root, root.val)
        return count
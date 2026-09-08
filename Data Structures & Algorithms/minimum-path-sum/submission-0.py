class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ans = grid.copy()
        for i in range(1, len(grid)):
            ans[i][0] += ans[i - 1][0]
        for i in range(1, len(grid[0])):
            ans[0][i] += ans[0][i - 1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                ans[i][j] += min(ans[i - 1][j], ans[i][j - 1])
        return ans[-1][-1]
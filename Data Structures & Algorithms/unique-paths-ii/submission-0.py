class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m = lines and n columns
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        arr = [[0 for i in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            arr[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                arr[i][0] = arr[i-1][0]
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                arr[0][i] = arr[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[-1][-1]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix), len(matrix[0])
        
        res = []
        for k in range((min(n,m) + 1) // 2):
            #top
            for i in range(k, m - k):
                res.append(matrix[k][i])
            #right
            for i in range(1 + k, n - k):
                res.append(matrix[i][m - 1 - k])
            #down
            for i in range(1 + k, m - k):
                res.append(matrix[n - 1 - k][m - 1 - i])
            #left
            for i in range(1 + k, n - k - 1):
                res.append(matrix[n - 1 - i][k])
        return res[:n * m]
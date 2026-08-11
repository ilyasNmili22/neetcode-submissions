class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        ret = n * [n * [0]]
        for i in range(n):
            ret[i] = [matrix[j][i] for j in range(n)][::-1] 
        print(ret)
        matrix[:] = ret
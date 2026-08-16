class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_r, new_c = len(matrix[0]), len(matrix)
        ret = [[0] * new_c for i in range(new_r)]

        for i in range(new_r):
            for j in range(new_c):
                ret[i][j] = matrix[j][i]
        return ret
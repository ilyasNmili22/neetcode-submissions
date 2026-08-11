class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        column_set = set()
        row_set = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    column_set.add(j)

        print(column_set, row_set)
        for x in row_set:
            matrix[x] = c * [0]
        for y in column_set:
            for i in range(r):
                matrix[i][y] = 0
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(1, len(matrix[0])):
            self.arr[0][i] += self.arr[0][i - 1]
        for i in range(1, len(matrix)):
            self.arr[i][0] += self.arr[i - 1][0]
            for j in range(1, len(matrix[0])):
                self.arr[i][j] = self.arr[i][j-1] + self.arr[i-1][j] - self.arr[i-1][j-1] + matrix[i][j]
        print(self.arr)
        return None


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return self.arr[row2][col2] - self.arr[row2][col1-1] - self.arr[row1-1][col2] + self.arr[row1-1][col1-1]
        elif row1 > 0:
            return self.arr[row2][col2]  - self.arr[row1-1][col2]
        elif col1 > 0:
            return self.arr[row2][col2] - self.arr[row2][col1-1] 
        else:
            return self.arr[row2][col2]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)




"""
3 3  4  8  10
8 14 18 24 27

self.arr[i][j] =  self.arr[i][j-1] + matrix[i][j] + self.arr[i-1][j] - self.arr[i - 1][j-1]

"""
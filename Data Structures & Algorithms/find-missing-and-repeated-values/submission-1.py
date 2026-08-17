class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i]))]
        arr.sort()
        a1, a2 = 0, 1
        print(arr)
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                a1 = arr[i]
            elif arr[i] - arr[i - 1] != 1:
                a2 = arr[i] - 1
        if a2 == 1 and arr[0] == 1:
            a2 = len(arr)
        return [a1, a2]
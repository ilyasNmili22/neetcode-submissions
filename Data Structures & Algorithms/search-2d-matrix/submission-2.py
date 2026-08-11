class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vect = [element for row in matrix for element in row]
        left, right = 0, len(vect) - 1
        while(left <= right):
            med = left + (right - left) // 2
            if vect[med] < target:
                left = med + 1
            elif vect[med] > target:
                right = med - 1
            else:
                return True
        return False

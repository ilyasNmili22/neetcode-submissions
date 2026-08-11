import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]   
                if num == '.':
                    continue
                if num in rows[r]:
                    return False
                rows[r].add(num)
                if num in cols[c]:
                    return False
                cols[c].add(num)
                box_index = (r // 3) * 3 + (c // 3) 
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        return True
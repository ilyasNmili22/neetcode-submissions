class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if (len(set(board[i])) + board[i].count('.') - int('.' in board[i]) != 9):
                return False
            column_i = [row[i] for row in board]
            if len(set(column_i)) + column_i.count('.') - int('.' in column_i) != 9:
                return False
        for i in range(0, 7, 3):
            for j in range(0,7,3):
                box = [row[j:j+3] for row in board[i:i + 3]]
                box_vect = [x for row in box for x in row] #Matrix to vector
                if len(set(box_vect)) + box_vect.count('.') - int('.' in box_vect) != 9:
                    return False
        return True 
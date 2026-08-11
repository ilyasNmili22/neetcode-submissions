class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, indx):
            if indx == len(word):
                return True
            if i < 0 or i >= len(board) or j >= len(board[0]) or j < 0 or indx > len(word) or (i, j) in visited:
                return False
            if board[i][j] != word[indx]:
                return False
            visited.add((i, j))
            found = dfs(i + 1, j, indx + 1) or dfs(i - 1, j, indx + 1) or dfs(i, j + 1, indx + 1) or dfs(i, j - 1, indx + 1)
            visited.remove((i, j))
            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        


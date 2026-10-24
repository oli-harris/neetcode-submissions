class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in range(9):
            seen = set()
            for i in range(9):
                node = board[row][i]
                if node == '.':
                    continue
                if node in seen:
                    return False
                seen.add(node)

        # check cols
        for col in range(9):
            seen = set()
            for i in range(9):
                node = board[i][col]
                if node == '.':
                    continue
                if node in seen:
                    return False
                seen.add(node)

        # check squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    node = board[row][col]
                    if node == '.':
                        continue
                    if node in seen:
                        return False
                    seen.add(node)

        return True
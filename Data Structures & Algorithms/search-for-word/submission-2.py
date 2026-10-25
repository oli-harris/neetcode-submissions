class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        seen = set([])

        def dfs(x, y, i):
            if i == len(word):
                return True

            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[i] or (x, y) in seen:
                return False

            seen.add((x, y))
            for dx, dy in DIRECTIONS:  
                nx, ny = x + dx, y + dy

                if dfs(nx, ny, i + 1):
                    return True

            seen.remove((x, y))
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True


        return False


            
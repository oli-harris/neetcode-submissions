class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        seen = set([])

        def dfs(x, y, i):
            if i == len(word):
                return True

            char = word[i]
            seen.add((x, y))
            
            for dx, dy in DIRECTIONS:  
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny] != char or (nx, ny) in seen:
                    continue
                if dfs(nx, ny, i + 1):
                    seen.remove((x, y))
                    return True

            seen.remove((x, y))

            return False

        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if dfs(x, y, 1):
                        return True


        return False


            
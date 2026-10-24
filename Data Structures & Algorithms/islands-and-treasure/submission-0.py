class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER = -1
        CHEST = 0
        INF = 2147483647

        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([])
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == CHEST:
                    queue.append((i, j))
                    visited.add((i, j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                grid[x][y] = dist

                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < ROWS and 0 <= ny < COLS):
                        continue

                    if grid[nx][ny] == WATER or (nx, ny) in visited:
                        continue

                    visited.add((nx, ny))
                    queue.append((nx, ny))
            
            dist += 1

                    
                


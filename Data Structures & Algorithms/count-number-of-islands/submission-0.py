class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        seen = set() # set of (row, col)
        islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0" or (i, j) in seen:
                    continue

                # Explore all of new island by BFS
                islands += 1
                queue = deque([(i,j)]) # (i,j)

                while queue:
                    nodeI, nodeJ = queue.pop()
                    
                    if (nodeI, nodeJ) in seen or grid[nodeI][nodeJ] == "0":
                        continue

                    if grid[nodeI][nodeJ] == "1":
                        seen.add((nodeI, nodeJ))

                    for a, b in DIRECTIONS:
                        nr, nc = (nodeI + a), (nodeJ + b)
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                            continue
                        
                        queue.append((nr, nc))
                    
        return islands


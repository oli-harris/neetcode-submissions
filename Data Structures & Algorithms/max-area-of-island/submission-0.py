class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        seen = set() # (i, j)
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen or grid[r][c] == 0:
                    continue

                # explore island by bfs
                area = 0
                queue = deque([(r,c)])

                while queue:
                    bR, bC = queue.popleft()

                    if (bR, bC) in seen or grid[bR][bC] == 0:
                        continue

                    area += 1
                    seen.add((bR, bC))
                    for dR, dC in directions:
                        nR, nC = (bR + dR), (bC + dC)
                        if nR >= 0 and nR < rows and nC >= 0 and nC < cols:
                            queue.append((nR, nC))

                maxArea = max(maxArea, area)

        return maxArea
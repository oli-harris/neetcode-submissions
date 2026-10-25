class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(stack):
            reachable = set()
            while stack:
                x, y = stack.pop()

                if (x, y) in reachable:
                    continue

                reachable.add((x, y))
                
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if heights[nx][ny] >= heights[x][y]:
                        stack.append((nx, ny))

            return reachable

        pacific = []
        atlantic = []
        for r in range(len(heights)):
            pacific.append((r, 0))
            atlantic.append((r, n - 1))
        
        for c in range(len(heights[0])):
            pacific.append((0, c))
            atlantic.append((m - 1, c))

        pacificReachable = dfs(pacific)
        atlanticReachable = dfs(atlantic)

        return [pos for pos in pacificReachable & atlanticReachable]




        
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def flood(sr, sc):
            q = deque([(sr, sc)])
            visited.add((sr, sc))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    flood(r, c)

        return count
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        fresh = 0
        q=deque()
        #scanning rottens
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2 :
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh +=1
        print(q, fresh)
        minutes = 0
        if fresh == 0 :
            return minutes
        
        while q :
            minutes+=1
            
            for _ in range(len(q)) :
                (r,c) = q.popleft()
                #check the 4 directions for these
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)] :
                    nr, nc = dr+r, dc+c
                    if 0<=nr<m and 0<=nc<n :
                        if grid[nr][nc] == 1 :
                            fresh-=1
                            if fresh == 0 :
                                return minutes
                            grid[nr][nc] = 2
                            q.append((nr, nc))
        
        return -1
        

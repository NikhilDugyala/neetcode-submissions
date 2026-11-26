class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        max_area = 0
        visit = set()
        def bfs(r, c):
            if (r not in range(rows)) or (c not in range(columns)) or grid[r][c]==0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            return (1 + bfs(r+1,c)+ bfs(r-1,c)+ bfs(r,c+1)+ bfs(r,c-1))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(area, max_area)
                    
        
        return max_area
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        max_area = 0
        visit = set()
        def bfs(r, c):
            area = 1
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows)) and (c in range(columns)) and grid[r][c]==1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                        area+=1
            return area
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(area, max_area)
                    
        
        return max_area
        
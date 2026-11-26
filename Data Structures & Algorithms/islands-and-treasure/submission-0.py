class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q= collections.deque()
        visit=set()
        level=1
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))


        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col= dr+r, dc+c
                    if row<0 or col<0 or row==ROWS or col==COLS or (row,col) in visit or grid[row][col]==-1:
                        continue
                    grid[row][col]=level
                    q.append((row,col))
                    visit.add((row,col))
                    
            level+=1





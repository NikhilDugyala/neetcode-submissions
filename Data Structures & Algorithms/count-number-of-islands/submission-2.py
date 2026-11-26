class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            # Base case: return if out of bounds or not land or already visited
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0" or 
                (r, c) in visit):
                return

            visit.add((r, c))
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands

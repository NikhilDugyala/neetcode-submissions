class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        borders = set()

        def dfs(r, c):
            # out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            # not an O or already visited
            if board[r][c] != "O" or (r, c) in borders:
                return

            borders.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # run DFS from all border cells
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # flip only non-border-connected O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in borders:
                    board[r][c] = "X"

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #  define the sets for each row, col and the subgrids
        row_sets= [ set() for _ in range(9)]
        col_sets= [ set() for _ in range(9)]
        subgrid_sets= [[ set() for _ in range(3)] for _ in range(3)]

        # now navigate the board
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num==".":
                    continue

                # cehck if num is present in sets
                if num in row_sets[r]:
                    return False
                
                if num in col_sets[c]:
                    return False
                
                if num in subgrid_sets[r//3][c//3]:
                    return False

                row_sets[r].add(num)
                col_sets[c].add(num)

                subgrid_sets[r//3][c//3].add(num)
        return True

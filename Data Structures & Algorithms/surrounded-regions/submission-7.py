class Solution:
    def solve(self, board: List[List[str]]) -> None:
        all_o_cells = set()
        edge_o_cells = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    all_o_cells.add((i, j))
                    if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                        edge_o_cells.add((i, j))
        
        def is_valid(cell):
            r, c = cell
            in_row_range = 0 <= r < len(board)
            in_col_range = 0 <= c < len(board[0])
            if in_row_range and in_col_range:
                if board[r][c] == "O":
                    return True
            return False

        visited = set()
        def dfs(cell):
            if cell in visited:
                return
            
            all_o_cells.remove(cell) # remove from all_o_cells as this came from an edge
            visited.add(cell) # add to the visited cells
            
            r, c = cell
            neighbors = [
                (r, c + 1),
                (r, c - 1),
                (r + 1, c),
                (r - 1, c)
            ]
            for neighbor in neighbors:
                if is_valid(neighbor):
                    dfs(neighbor)
        
        for edge_o_cell in edge_o_cells:
            if edge_o_cell in visited:
                continue
            dfs(edge_o_cell)
        
        for remaining_cell in all_o_cells:
            rr, rc = remaining_cell
            board[rr][rc] = "X"
        
        


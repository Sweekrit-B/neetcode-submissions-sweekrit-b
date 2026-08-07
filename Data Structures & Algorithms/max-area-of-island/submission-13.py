class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        all_land_cells = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    all_land_cells.add((i, j))
        # print(all_land_cells)
        
        def is_valid(row, col, visited):
            row_in_range = 0 <= row < len(grid)
            col_in_range = 0 <= col < len(grid[0])
            if row_in_range and col_in_range:
                cell_is_island = grid[row][col] == 1
                in_visited = (row, col) in visited
                if cell_is_island and not in_visited:
                    return True
            return False
        
        visited = set()
        island_size = 1

        def dfs(cell):
            nonlocal visited
            nonlocal island_size
            
            row, col = cell
            neighbors = [
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col)
            ]
            for neighbor in neighbors:
                neighbor_row, neighbor_col = neighbor
                if is_valid(neighbor_row, neighbor_col, visited):
                    visited.add(neighbor)
                    island_size += 1
                    dfs(neighbor)
        
        max_island_size = 0
        for land_cell in all_land_cells:
            if land_cell not in visited:
                # reset current island size
                island_size = 1
                # add to visited
                visited.add(land_cell)
                # run the dfs
                dfs(land_cell)
                # determine if the island has grown
                max_island_size = max(island_size, max_island_size)
        
        return max_island_size
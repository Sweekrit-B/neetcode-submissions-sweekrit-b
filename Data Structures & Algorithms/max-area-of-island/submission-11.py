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

        def bfs(start):
            visited = set()
            queue = deque()
            queue.append(start)
            visited.add(start)
            island_size = 1
            while len(queue) > 0:
                for i in range(len(queue)): # for all items currently in the queue
                    cell = queue.popleft() # grab each item
                    # print(cell)
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
                            island_size += 1
                            queue.append(neighbor)
                            visited.add(neighbor)
            return island_size, visited
        
        max_island_size = 0
        overall_visited = set()
        for land_cell in all_land_cells:
            # print(land_cell)
            if land_cell in overall_visited:
                continue
            island_size, visited_land_cells = bfs(land_cell)
            overall_visited.update(visited_land_cells)
            max_island_size = max(max_island_size, island_size)

        return max_island_size

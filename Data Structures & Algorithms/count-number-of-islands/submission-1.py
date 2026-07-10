class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start by recording where every cell is 1 --> O(n * m)
        # for every cell that is 1 --> do a BFS algorithm until no other value is found --> O(n * m + 4 * n * m) = O(n * m)
        # once the cells that could be 1 is empty --> number of islands

        all_island_cells = set()
        for i in range(len(grid)): # for every row
            for j in range(len(grid[0])): # for every col
                if grid[i][j] == "1":
                    all_island_cells.add((i, j))

        # print("All island cells before processing: ", all_island_cells)
        num_islands = 0

        while len(all_island_cells) > 0:
            curr_queue = deque([all_island_cells.pop()])
            # print("Starting cell of this run: ", curr_queue)
            visited = set()

            while len(curr_queue) > 0:
                current_cell = curr_queue.popleft()
                visited.add(current_cell)
                if current_cell in all_island_cells:
                    all_island_cells.remove(current_cell)

                neighbors = [
                    (current_cell[0] + 1, current_cell[1]),
                    (current_cell[0] - 1, current_cell[1]),
                    (current_cell[0], current_cell[1] + 1),
                    (current_cell[0], current_cell[1] - 1)
                ]

                for neighbor in neighbors:
                    if neighbor in all_island_cells and neighbor not in visited:
                        curr_queue.append(neighbor)
            
            # print("All island cells visited while processing: ", visited)
            # print("All remaining island cells: ", all_island_cells)

            num_islands += 1
            # print("Number of islands", num_islands)

        # print("Final island cells: ", all_island_cells)
        return num_islands
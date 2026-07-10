#BFS

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        all_island_cells = set()
        for i in range(len(grid)): # for every row
            for j in range(len(grid[0])): # for every col
                if grid[i][j] == 1:
                    all_island_cells.add((i, j))

        # print("All island cells before processing: ", all_island_cells)
        max_island_area = 0

        while len(all_island_cells) > 0:
            curr_queue = deque([all_island_cells.pop()])
            # print("Starting cell of this run: ", curr_queue)
            visited = set()

            while len(curr_queue) > 0:
                current_cell = curr_queue.popleft()
                visited.add(current_cell)

                neighbors = [
                    (current_cell[0] + 1, current_cell[1]),
                    (current_cell[0] - 1, current_cell[1]),
                    (current_cell[0], current_cell[1] + 1),
                    (current_cell[0], current_cell[1] - 1)
                ]

                for neighbor in neighbors:
                    if neighbor in all_island_cells and neighbor not in visited:
                        all_island_cells.remove(neighbor)
                        curr_queue.append(neighbor)
            
            # print("All island cells visited while processing: ", visited)
            # print("All remaining island cells: ", all_island_cells)

            max_island_area = max(max_island_area, len(visited))
            # print("Max island area: ", max_island_area)

        # print("Final island cells: ", all_island_cells)
        return max_island_area
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        all_island_cells = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    all_island_cells.add((i, j))
        # print(all_island_cells)

        max_island_area = 0

        while len(all_island_cells) > 0:
            curr_queue = deque([all_island_cells.pop()])
            visited = set() # initialize for the current run

            while len(curr_queue) > 0:
                curr_cell = curr_queue.pop()
                visited.add(curr_cell)

                row, col = curr_cell
                neighbors = [
                    (row, col + 1),
                    (row, col - 1),
                    (row + 1, col),
                    (row - 1, col)
                ]

                for neighbor in neighbors:
                    if neighbor in all_island_cells and neighbor not in visited:
                        all_island_cells.remove(neighbor)
                        curr_queue.append(neighbor)
            
            max_island_area = max(max_island_area, len(visited))
        
        return max_island_area
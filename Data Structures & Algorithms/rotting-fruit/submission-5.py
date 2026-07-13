class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # rot time - BFS algorithm
        rot_queue = deque()
        time_taken = 0

        # function to check if a cell is valid
        def valid_cell(cell):
            row, col = cell
            # check to be within grid constraints
            if (row < 0) or (row >= len(grid)) or (col < 0) or (col >= len(grid[0])):
                return False
            # check to make sure there's a fresh fruit in the cell
            if (grid[row][col] == 0) or (grid[row][col] == 2):
                return False
            return True
        
        # all fresh fruit + rot queue population
        all_fresh_fruit = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    all_fresh_fruit += 1
                if grid[row][col] == 2:
                    rot_queue.append((row, col))
        
        if all_fresh_fruit == 0:
            return 0

        # BFS algorithm
        while len(rot_queue) > 0:
            
            for _ in range(len(rot_queue)):
                # get the first rotting fruit from the queue
                curr_fruit = rot_queue.popleft()
                # get all neighbors
                neighbors = [
                    (curr_fruit[0] + 1, curr_fruit[1]),
                    (curr_fruit[0] - 1, curr_fruit[1]),
                    (curr_fruit[0], curr_fruit[1] + 1),
                    (curr_fruit[0], curr_fruit[1] - 1)
                ]
                # mark the neighbors as rotting
                for neighbor in neighbors:
                    # if the fruit is valid
                    if valid_cell(neighbor):
                        # mark the current fruit as rotten
                        grid[neighbor[0]][neighbor[1]] = 2
                        # add to rot queue
                        rot_queue.append(neighbor)
                        # subtract from the amount of fresh fruit left
                        all_fresh_fruit -= 1

            # add one to the amount of time taken
            time_taken += 1

            # return time taken if all fresh fruit are gone
            if all_fresh_fruit == 0:
                return time_taken

        return -1
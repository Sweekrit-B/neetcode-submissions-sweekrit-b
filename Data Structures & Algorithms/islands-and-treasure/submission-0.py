class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Step 1: find all treasure chests
        # Step 2: for each treasure chest, run a BFS algorithm marking each cell
        # Step 3: if the distance calculated is < current distance, update cell

        treasure_chests = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasure_chests.append((row, col))
        
        def validate_neighbor(neighbor):
            row, col, distance = neighbor
            # if the cell is in bounds
            if (row >= len(grid)) or (row < 0) or (col >= len(grid[0]) or (col < 0)):
                return False
            # if the distance to the cell is not less than the cell's current value
            if distance >= grid[row][col]:
                return False
            return True

        for treasure in treasure_chests:
            # Create an empty queue and an empty set
            queue = deque()
            visited = set()

            # Append the first element to both
            queue.append((treasure[0], treasure[1], 0))
            visited.add((treasure[0], treasure[1]))

            # While the queue is not empty...
            while len(queue) > 0:
                # print("Current queue: ", queue)
                # Get the most recent element
                curr_square = queue.popleft()
                # print("Current square being looked at: ", curr_square)
                # Get the distance from the treasure for every square next to it
                curr_distance = curr_square[2] + 1
                # print("Current distance being calculated: ", curr_distance)

                # Calculate all the neighbors
                neighbors = [
                    (curr_square[0] + 1, curr_square[1], curr_distance),
                    (curr_square[0] - 1, curr_square[1], curr_distance),
                    (curr_square[0], curr_square[1] + 1, curr_distance),
                    (curr_square[0], curr_square[1] - 1, curr_distance)
                ]
                # print("All neighbor options: ", neighbors)

                # For each neighbor
                for neighbor in neighbors:
                    # print("Checking neighbor: ", neighbor)
                    neighbor_cell = (neighbor[0], neighbor[1])
                    # Check if the square ITSELF has been visited already
                    if neighbor_cell not in visited and validate_neighbor(neighbor):
                        # print(f"Neighbor {neighbor} is valid")
                        # Add the neighboring square to visited
                        visited.add((neighbor[0], neighbor[1]))
                        # print(f"Added {(neighbor[0], neighbor[1])} to visited set")
                        # Set the current distance in the actual grid
                        grid[neighbor[0]][neighbor[1]] = curr_distance
                        # print(f"Setting {(neighbor[0], neighbor[1])} to {curr_distance}")
                        # Add neighbor to queue
                        queue.append(neighbor)

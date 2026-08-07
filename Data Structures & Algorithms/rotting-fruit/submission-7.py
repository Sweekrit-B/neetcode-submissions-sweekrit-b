class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_fruit = 0
        rotten_fruit = deque()
        time = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotten_fruit.append((i, j))
                if grid[i][j] == 1:
                    fresh_fruit += 1
            
        if fresh_fruit == 0:
            return 0
        
        while rotten_fruit:
                for i in range(len(rotten_fruit)):
                    curr_fruit = rotten_fruit.popleft()
                    
                    neighbors = [
                        (curr_fruit[0] + 1, curr_fruit[1]),
                        (curr_fruit[0] - 1, curr_fruit[1]),
                        (curr_fruit[0], curr_fruit[1] + 1),
                        (curr_fruit[0], curr_fruit[1] - 1)
                    ]

                    print(neighbors)

                    for neighbor in neighbors:
                        if ((0 <= neighbor[0] < ROWS) and (0 <= neighbor[1] < COLS) 
                            and grid[neighbor[0]][neighbor[1]] == 1):
                            grid[neighbor[0]][neighbor[1]] = 2
                            fresh_fruit -= 1
                            rotten_fruit.append(neighbor)
                
                time += 1
                if fresh_fruit == 0:
                    return time
        
        return -1
        
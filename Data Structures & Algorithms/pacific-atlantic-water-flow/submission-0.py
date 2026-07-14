class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac_border_squares = set()
        atl_border_squares = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i == 0) or (j == 0):
                    pac_border_squares.add((i, j))
                if (i == len(heights) - 1) or (j == len(heights[0]) - 1):
                    atl_border_squares.add((i, j))
    
        def cell_valid(square, ref_height):
            row, col = square
            if (row < 0) or (row >= len(heights)) or (col < 0) or (col >= len(heights[0])):
                return False
            if heights[row][col] > ref_height:
                return False
            return True

        def dfs(square, pac_touched, atl_touched, visited):
            row, col = square

            if square in pac_border_squares:
                pac_touched = 1
            if square in atl_border_squares:
                atl_touched = 1
            
            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]

            for neighbor in neighbors:
                if cell_valid(neighbor, heights[row][col]) and neighbor not in visited:
                    visited.add(neighbor)
                    pac_touch_neighbor, atl_touch_neighbor = dfs(neighbor, pac_touched, atl_touched, visited)
                    pac_touched = max(pac_touched, pac_touch_neighbor)
                    atl_touched = max(atl_touched, atl_touch_neighbor)
            
            return pac_touched, atl_touched
        
        result = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                square_set = set()
                pac_touched, atl_touched = dfs((i, j), False, False, square_set)
                if pac_touched and atl_touched:
                    result.append([i, j])
        
        return result
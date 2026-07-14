class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach_pacific = set()
        can_reach_atlantic = set()

        def cell_valid(square, ref_height):
            row, col = square
            if (row < 0) or (row >= len(heights)) or (col < 0) or (col >= len(heights[0])):
                return False
            if heights[row][col] < ref_height: # check flow upward
                return False
            return True


        def dfs(square, visited):
            row, col = square

            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]

            for neighbor in neighbors:
                if cell_valid(neighbor, heights[row][col]) and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited)
            
            return
        
        pac_border_squares = set()
        atl_border_squares = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i == 0) or (j == 0):
                    pac_border_squares.add((i, j))
                if (i == len(heights) - 1) or (j == len(heights[0]) - 1):
                    atl_border_squares.add((i, j))
        
        for pac_square in pac_border_squares:
            dfs(pac_square, can_reach_pacific)
        for atl_square in atl_border_squares:
            dfs(atl_square, can_reach_atlantic)
        
        result_set = can_reach_pacific.intersection(can_reach_atlantic)
        result_set.add((len(heights) - 1, 0))
        result_set.add((0, len(heights[0]) - 1))
        final_result = []
        for result in result_set:
            final_result.append(result)

        return final_result
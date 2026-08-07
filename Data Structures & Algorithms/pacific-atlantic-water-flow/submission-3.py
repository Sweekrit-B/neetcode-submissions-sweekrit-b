class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # there are two ways we can go about this
            # starting from each square, we can run a script to do a DFS until it reaches either ocean
                # we would go either to the same height or lower
            # starting from each ocean, we do a DFS, and get the intersection of the two sets
                # we would go to the same height or higher
                # more efficient, as it is checking less items
        
        pacific_set = set()
        atlantic_set = set()

        def is_valid(cell, parent):
            r, c = cell
            pr, pc = parent
            in_row_range = 0 <= r < len(heights)
            in_col_range = 0 <= c < len(heights[0])
            if in_row_range and in_col_range:
                if heights[pr][pc] <= heights[r][c]: # equal or higher
                    return True

        def dfs(cell, ocean):
            nonlocal pacific_set
            nonlocal atlantic_set

            if ocean == "pacific":
                if cell in pacific_set:
                    return
                pacific_set.add(cell)

            if ocean == "atlantic":
                if cell in atlantic_set:
                    return
                atlantic_set.add(cell)
            
            r, c = cell
            neighbors = [
                (r, c + 1),
                (r, c - 1),
                (r + 1, c),
                (r - 1, c)
            ]

            for neighbor in neighbors:
                if is_valid(neighbor, cell):
                    dfs(neighbor, ocean)

            return
        
        all_pacific_cells = set()
        all_atlantic_cells = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    all_pacific_cells.add((i, j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    all_atlantic_cells.add((i, j))
        
        for pacific_cell in all_pacific_cells:
            if pacific_cell in pacific_set:
                continue
            dfs(pacific_cell, "pacific")
        
        for atlantic_cell in all_atlantic_cells:
            if atlantic_cell in atlantic_set:
                continue
            dfs(atlantic_cell, "atlantic")
        
        res = []
        for cell in pacific_set.intersection(atlantic_set):
            res.append(list(cell))
        
        return res
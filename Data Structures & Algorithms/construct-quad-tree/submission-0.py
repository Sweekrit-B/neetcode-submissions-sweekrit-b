"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# sub-problems that we have to solve
    # step 1: how to divide the grid into 4
    # step 2: how to determine whether all values in the grid are the same (if we have a leaf)
    # step 3: recurse through and continue this process 

class Solution:
    def check(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        curr_val = grid[0][0]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != curr_val:
                    return (False, 1)
        return (True, curr_val)

    def divide(self, grid: List[List[int]]) -> List[List[List[int]]]:
        ROWS, COLS = len(grid), len(grid[0])
        row_divider = ROWS // 2 # anything >= is on the bottom
        col_divider = COLS // 2 # anything >= is on the right
        top_left = []
        top_right = []
        bottom_left = []
        bottom_right = []
        for i in range(ROWS):
            left_row = []
            right_row = []
            for j in range(COLS):
                if j < col_divider:
                    left_row.append(grid[i][j])
                else:
                    right_row.append(grid[i][j])
            if i < row_divider:
                top_left.append(left_row)
                top_right.append(right_row)
            else:
                bottom_left.append(left_row)
                bottom_right.append(right_row)
        return [top_left, top_right, bottom_left, bottom_right]

                
    def construct(self, grid: List[List[int]]) -> 'Node':
        check = self.check(grid)
        if check[0]:
            return Node(check[1], True) # return a leaf with the appropriate value
        else:
            top_left, top_right, bottom_left, bottom_right = self.divide(grid)
            top_left_node = self.construct(top_left)
            top_right_node = self.construct(top_right)
            bottom_left_node = self.construct(bottom_left)
            bottom_right_node = self.construct(bottom_right)
            return Node(check[1], False, top_left_node, top_right_node, bottom_left_node, bottom_right_node)
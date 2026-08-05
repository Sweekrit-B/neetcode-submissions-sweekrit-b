class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_unique_nums(line):
            nums = set()
            for num in line:
                if num in nums and num != '.':
                    return False
                nums.add(num)
            return True
        
        # check every row
        for row_ix in range(len(board)):
            if not check_unique_nums(board[row_ix]):
                return False

        # create dicts for column and grid
        cols_dict = defaultdict(list)
        grid_dict = defaultdict(list)
        for row_ix in range(len(board)):
            for col_ix in range(len(board[0])):
                cols_dict[col_ix].append(board[row_ix][col_ix])
                grid_dict[(row_ix // 3, col_ix // 3)].append(board[row_ix][col_ix])
        
        # check every column
        for col_ix in cols_dict:
            if not check_unique_nums(cols_dict[col_ix]):
                return False

        # check every grid
        for grid_ix in grid_dict:
            if not check_unique_nums(grid_dict[grid_ix]):
                return False
        
        return True
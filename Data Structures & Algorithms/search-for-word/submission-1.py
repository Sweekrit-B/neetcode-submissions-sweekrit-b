class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # at any given point, track already iterated cells + look at neighboring cells
        # start with a given point for the first letter
        # if the neighbors have second letter, add those neighbors to "potential"
        # do dfs on each of these "potential" options

        max_row_index = len(board)
        max_col_index = len(board[0])

        def dfs(curr_row, curr_col, curr_letter_index, already_iterated_positions):
            if curr_letter_index == len(word) - 1: # if the word is complete
                return True
            
            neighbors = [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)] # get all neighbors
            valid_neighbors = []
            
            for neighbor in neighbors:
                # ignore out-of-range neighbors
                if (neighbor[0] not in range(0, max_row_index)) or (neighbor[1] not in range(0, max_col_index)):
                    continue
                # ignore neighbors that already have been seen
                if neighbor in already_iterated_positions:
                    continue
                # if valid, then add to valid neighbors
                if board[neighbor[0]][neighbor[1]] == word[curr_letter_index + 1]:
                    valid_neighbors.append(neighbor)
            
            if len(valid_neighbors) == 0:
                # if there is no valid neighbors, this is not a valid word
                return False
            
            for neighbor in valid_neighbors:
                # if any of the neighbors iterations return a successful result
                if dfs(neighbor[0], neighbor[1], curr_letter_index + 1, already_iterated_positions + [neighbor]):
                    return True
            
            return False
        
        starting_positions = []
        starting_letter = word[0]
        for i in range(max_row_index):
            for j in range(max_col_index):
                if board[i][j] == starting_letter:
                    starting_positions.append((i, j))
        
        for starting_position in starting_positions:
            if dfs(starting_position[0], starting_position[1], 0, [starting_position]):
                return True
        
        return False
        


                
            
        
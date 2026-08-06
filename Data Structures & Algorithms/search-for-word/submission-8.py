class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking
        starting_indices = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starting_indices.append((i, j))
        print(starting_indices)
        
        def check_in_range(i, j):
            if (0 <= i < len(board)) and (0 <= j < len(board[0])):
                return True

        visited = set()
        def dfs(i, j, word_ix):
            if word_ix >= len(word) - 1:
                return True
            neighbors = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1)
            ]
            for neighbor in neighbors:
                next_i, next_j = neighbor
                if check_in_range(next_i, next_j):
                    # print(f"Neighbor value: {board[next_i][next_j]} at index {(next_i, next_j)}")
                    if board[next_i][next_j] == word[word_ix + 1] and (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))
                        # print(f"ADDED {neighbor} to visited: {visited}\n")
                        if dfs(next_i, next_j, word_ix+1):
                            # print(f"Found next elem {word[word_ix+1]} at {next_i, next_j}")
                            return True
                        visited.remove((next_i, next_j))
                        # print(f"POPPING {neighbor} from visited: {visited}\n")
            # print(f"UNABLE to find {word[word_ix+1]} from {word[word_ix]}")
            return False
        
        for start_i, start_j in starting_indices:
            # print(f"\nStarting at {board[start_i][start_j]} at index {(start_i, start_j)}\n")
            visited.add((start_i, start_j))
            if dfs(start_i, start_j, 0):
                return True
            visited.remove((start_i, start_j))

        return False

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # step 1: get all O squares, and also a set of O squares at the edges
        # step 2: from each O square at the edge, do a DFS/BFS of other O squares
        # step 3: for each square that is connected to an O square at the edge, remove it from "all O squares" and "squares at the edge"
        # step 4: for the remaining squares, turn them into Xs

        all_o_squares = set()
        edge_o_squares = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if (i == 0) or (j == 0) or (i == len(board) - 1) or (j == len(board[0]) - 1):
                        edge_o_squares.add((i, j))
                    all_o_squares.add((i, j))

        def dfs(square):
            row, col = square

            neighbors = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            ]

            # for each neighboring square, just check if its still in all_o_squares
            for neighbor in neighbors:
                if neighbor in all_o_squares:
                    all_o_squares.remove(neighbor)
                    if neighbor in edge_o_squares:
                        edge_o_squares.remove(neighbor)
                    dfs(neighbor)
        
        print(f"Initial all O squares: {all_o_squares}")

        while len(edge_o_squares) > 0:
            curr_square = edge_o_squares.pop()
            all_o_squares.remove(curr_square)
            print(f"Looking at: {curr_square}")
            dfs(curr_square)
        
        print(f"Final all O squares: {all_o_squares}")

        for remaining_square in all_o_squares:
            row, col = remaining_square
            board[row][col] = "X"
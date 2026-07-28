class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0:
                    # print(f"Assigning {(i, j)} to 1")
                    num_paths[i][j] = 1
                elif j == 0:
                    # print(f"Assigning {(i, j)} to 1")
                    num_paths[i][j] = 1
                elif i == 0 and j == 0:
                    # print(f"Assigning {(i, j)} to 0")
                    num_paths[i][j] = 0
                else:
                    num_paths[i][j] = num_paths[i-1][j] + num_paths[i][j-1]
                    # print(f"Assigning {(i, j)} to {num_paths[i][j]}")
        return num_paths[-1][-1]
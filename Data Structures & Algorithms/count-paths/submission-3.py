class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # at any given point, you can either come from left or up
        # sum all the values there
        paths = [[0] * n for i in range(m)]
        for i in range(len(paths)):
            for j in range(len(paths[0])):
                if i == 0:
                    paths[i][j] = 1
                elif j == 0:
                    paths[i][j] = 1
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        
        return paths[-1][-1]
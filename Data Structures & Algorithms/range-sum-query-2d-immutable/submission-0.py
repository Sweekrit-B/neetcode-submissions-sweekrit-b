class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                curr_sum = matrix[r][c]
                if r > 0:
                    curr_sum += self.prefix_sum_matrix[r-1][c]
                if c > 0:
                    curr_sum += self.prefix_sum_matrix[r][c-1]
                if r > 0 and c > 0:
                    curr_sum -= self.prefix_sum_matrix[r-1][c-1]
                self.prefix_sum_matrix[r][c] = curr_sum
        
        # print(self.prefix_sum_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr_sum = self.prefix_sum_matrix[row2][col2]
        if row1 > 0:
            curr_sum -= self.prefix_sum_matrix[row1-1][col2]
        if col1 > 0:
            curr_sum -= self.prefix_sum_matrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            curr_sum += self.prefix_sum_matrix[row1-1][col1-1]
        return curr_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# observations
# record a val at every square that is it's sum from (0, 0) to (r, c)
    # do this by doing a prefix sum and doing (r-1, c) + (r, c-1) - (r-1, c-1) 
# to find the sum
    # find (r1-1, c2), (r2, c1-1), and (r1-1, c1-1)
    # sum inside rectangle is (r2, c2) - (r1-1, c2) - (r2, c1-1) + (r1-1, c1-1)
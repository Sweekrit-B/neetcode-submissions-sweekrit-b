class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # since we are searching for a target, my first instinct is to do binary search
        # from here, we can see that there are two main binary searches that we have
            # step 1: finding the row that the value is in
            # step 2: finding the value within that row
        
        ROWS, COLS = len(matrix), len(matrix[0])

        # step 1: finding the row
            # logic: we have to binary search from index 0 to index ROWS-1
            # we are searching for the minimum value ABOVE the target
            # for each value, if it is less than our target, then we move l -> m + 1
            # if it is greater or equal to target, then we move r -> m, as m could also potentially be the last element in the row
            # we do this as long as l < r --> once they are the same value or l is greater, just return r
        
        l = 0
        r = ROWS-1
        while l < r:
            m = ((l + r) // 2)
            if matrix[m][-1] < target:
                l = m + 1
            else:
                r = m
        row_interest = matrix[r]
        # print(row_interest)

        # step 2: finding the value within the row
            # logic: binary search from index 0 to index COLS-1
            # we are searching for the value itself
            # for each value, if it is less than our target, we move l -> m + 1
            # if it is equal to our target, we return True
            # if it is greater than our target, we move r -> m
            # we do this as long as l < r --> if by that point we have not returned True, just return False
        
        l2 = 0
        r2 = COLS-1
        while l2 < r2:
            m2 = ((l2 + r2) // 2)
            if row_interest[m2] == target:
                return True
            elif row_interest[m2] < target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        
        return row_interest[r2] == target
                
        
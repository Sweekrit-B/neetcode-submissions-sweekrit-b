class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start with a left and right pointer
        # when would the left pointer move?
            # is the right pointer * (width - 1) > curr?
                # the reason we only check right pointer is because the maximum height of any bucket formed is the right pointer
                # if yes, then move left pointer forward
                # recalculate curr
        # when would right pointer move?
            # is the left pointer * (width - 1) > curr?
                # the reason we only check left pointer is because the maximum height of any bucket formed from now is the left pointer
                # if yes, move right pointer backward
                # recalculate curr

        # example: [1, 7, 2, 5, 4, 7, 3, 6]
        # height[l] = 1, curr = 1 * (r - l) = 7
        # l = 0, r = 7
            # is height[r] * (r-l-1) > 7
                # 6 * 6 = 36 > 7 --> move l = 1
                # curr = min(height[l], height[r]) * (r - l - 1) = 36
        # l = 1, r = 7
            # is height[l] * (r-l-1) > 36
                # 7 * 5 = 35 < 36 --> don't move r
                # curr stays the same
        # l = 2, r = 7
            # is height[r] * (r-l-1) > 36
                # 6 * 4 = 24 < 36 --> don't more l
                # curr stays the same
        # since both r and l cannot be moved -> return curr

        l, r = 0, len(heights)-1
        curr_area = 0

        while l < r:
            curr_area = max(curr_area, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
        
        return curr_area


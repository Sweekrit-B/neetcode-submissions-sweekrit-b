class Solution:
    def trap(self, height: List[int]) -> int:
        # at any given index, the amount of water that can be held is the minimum of the maximum on the left side and the maximum on the right side
        # therefore, calculate the maximums from both ends, and then calculate the area at each index

        # v = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

        # l = [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
        # r = [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]

        # a = [0, 0, 2, 0, 2, 3, 2, 0, 0, 0]

        left = []
        curr_max_left = 0
        right = []
        curr_max_right = 0

        for i in range(len(height)):
            left.append(curr_max_left)
            if height[i] > curr_max_left:
                curr_max_left = height[i]
        
        for i in range(len(height)-1, -1, -1):
            right.append(curr_max_right)
            if height[i] > curr_max_right:
                curr_max_right = height[i]
        
        right = right[::-1]
        area = []
        for i in range(len(height)):
            area.append(max(0, min(left[i], right[i]) - height[i]))
        
        # print(height)
        # print(left)
        # print(right)
        # print(area)
        
        return sum(area)
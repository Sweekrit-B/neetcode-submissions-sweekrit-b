class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        l, r = 0, len(height)-1
        maxL = 0
        maxR = 0
        area = 0

        # we move whichever pointer is less
        # this is because if L is less than R, then we want the min(L, R), so the water at the position is going to be L - the height at that poisiton anyway

        while l < r:
            if height[l] <= height[r]:
                area += max(0, maxL - height[l])
                # print(f"Looking at {height[l]} compared to {maxL}, adding to area: {area}")
                maxL = max(height[l], maxL)
                l += 1
            else:
                area += max(0, maxR - height[r])
                # print(f"Looking at {height[r]} compared to {maxR}, adding to area: {area}")
                maxR = max(height[r], maxR)
                r -= 1
        
        return area
            

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # initial thoughts
            # we are essentially want to keep track of two things
            # the height of the rectangle, and the width of the rectangle
            # then, as we add elements, we compare two things:
                # if we added this bar and used the height of this bar to make a rectangle, what would be the size of the rectangle --> then, we can calculate the area of the rectangle
        # at any given point, we want to compute the left and right boundaries
            # l = [0, 0, 2, 3, 4, 5]
            # r = [1, 3, 3, 4, 5, 6]
            # [7] --> l = 0, r = 1
            # [7, 1] -> since 1 is less than 7, we will :
                # keep r = 1 for 7
                # pop 7 from the stack
                # assign l = 0 (the popped value) for 1
            # [1, 7] -> since 7 is greater than 1, we will :
                # assign r = 3 for 1
                # keep l = 2 for 7
                # keep r = 3 for 7
            # [1, 7, 2] -> since 2 is less than 7 but greater than 1, we will :
                # keep r = 3 for 7
                # pop 7 from the stack
                # assign r = 4 for 1 and keep r = 4 for 2
        
        # might be easier to go backwards, so that we are not repeating work
            # r = [5, 5, 5, 2, 5, 0]
            # l = [4, 1, 1, 1, -1, -1]
            # val = [4, 2, 2, 7, 1, 7]
            # [(4, 5)] -> r = 5
            # [(4, 5), (2, 4)] -> since 2 < 4, l for 4 = 4, r for 2 = 5 -> pop value to get [(2, 4)]
            # [(2, 4), (2, 3)] -> since 2 == 2, r for 2 = 5
            # [(2, 4), (2, 3), (7, 2)] -> since 7 > 2, r for 7 = 2
            # [(2, 4), (2, 3), (7, 2), (1, 1)] -> 
                # while 1 is less than stack.pop()
                    # l = 1 for all those values
                # r = last popped value (anything before that would have been inaccessible)
            # [(1, 1), (7, 0)] -> since 7 > 1, r for 7 = 0
            # for all remaining elements:
                # l = -1
        
        # logic
        # stack var
        # if stack is empty and (i, val) is added
            # r[i] = i
        # if (i, val) is added that is less than stack[-1]:
            # while can pop:
                # i_pop, val_pop
            # at the very end
            # l[i_pop] = i
            # r[i] = r[i_pop]
        # if (i, val) is added that is greater than stack[-1]:
            # r[i] = i
        # for all remaining elements, set l = -1

        # stack stores (val, i)
        r = [None] * len(heights)
        l = [None] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            val = heights[i]
            # print(f"\nLooking at {val} at index {i}")

            if not stack or val > stack[-1][0]:
                r[i] = i
                stack.append((val, i))
                # print(f"New right array: {r}")
                # print(f"New stack: {stack}")
            elif stack[-1][0] == val:
                r[i] = r[stack[-1][1]]
                stack.append((val, i))
                # print(f"New right array: {r}")
                # print(f"New stack: {stack}")
            
            while stack and val < stack[-1][0]:
                val_pop, i_pop = stack.pop()
                # print(f"Popped {val_pop, i_pop} to make {stack}")
                l[i_pop] = i
                # print(f"New left array: {l}")
                r[i] = r[i_pop]
                # print(f"New right array: {r}")
            stack.append((val, i))
            # print(f"New stack: {stack}")

        for i in range(len(l)):
            if l[i] == None:
                l[i] = -1
        
        # print(f"\nLeft indices: {l}")
        # print(f"Right indices: {r}")

        width = [r[i] - l[i] for i in range(len(l))]

        # print(f"Rectangle widths: {width}")

        area = [width[i] * heights[i] for i in range(len(width))]

        # print(f"Rectangle areas: {area}")

        return max(area)
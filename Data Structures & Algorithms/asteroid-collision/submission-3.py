class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # as you move through the array to the right
            # add asteroids that are positive to the stack
        # if you come across a negative asteroid
            # squish all smaller asteroids until you cannot anymore
            # then, once the negative asteroid has been destroyed or there is no more TO destroy, move
        # return the stack at the end

        stack = []
        for asteroid in asteroids:
            # print(f"Current asteroid: {asteroid}")
            if asteroid > 0:
                stack.append(asteroid)
                # print(f"New stack: {stack}")
            else:
                while stack and stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    # print(f"New stack after pop: {stack}")
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                    # print(f"New stack after append: {stack}")
                if stack and asteroid == -stack[-1]:
                    stack.pop()
                    # print(f"New stack after another pop: {stack}")
        return stack
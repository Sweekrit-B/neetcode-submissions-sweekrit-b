class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # pattern: monotonic decreasing stack starting from the beginning

        res = [0] * len(temperatures)
        stack = []

        for i, currVal in enumerate(temperatures):
            # print(f"Looking at index {i} and value {currVal}")
            while stack and stack[-1][0] < currVal:
                currVal_pop, i_pop = stack.pop()
                # print(f"Popped index: {i_pop}, popped value: {currVal_pop}")
                res[i_pop] = i - i_pop
            
            stack.append((currVal, i))
            # print(f"Results: {res}, stack: {stack}")
        
        return res
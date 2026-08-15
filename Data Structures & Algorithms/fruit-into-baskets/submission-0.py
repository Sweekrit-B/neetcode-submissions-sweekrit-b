class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # problem boils down to: what is the largest subarray that only contains two values?
        # brute force: start from the beginning, create subarray until condition fails, repeat process
        # alternative: we use a similar approach to brute force, but skip failures
            # observation: lets say we have something like [1, 2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 2, ....]
            # in this case, once we hit 3, we know we reached a failure point
            # however, we don't really need to check from index 1 onwards - we just need to check at the start of the last streak of "2"s
            # this way, the maximum amount of times we check every given value is twice - once when it is possibly ending our basket collection, and once when it's potentially starting it
        # problem type: variable sliding window
        
        l = 0
        curr_streak_fruit = fruits[0]
        curr_streak_start_ix = 0
        fruits_seen = set()
        fruits_seen.add(fruits[0])
        max_len = 0

        for r in range(len(fruits)):
            # when do you keep going?
            if fruits[r] in fruits_seen or len(fruits_seen) < 2:
                # print(f"The fruit {fruits[r]} is valid in the current baskets, adding: {fruits[l:r+1]}")
                # add to fruits seen
                fruits_seen.add(fruits[r])
                # print(f"Added to our seen fruits: {fruits_seen}")
                # when do you update your curr_streak_fruit?
                if curr_streak_fruit != fruits[r]:
                    # print(f"We have a new streak start!")
                    curr_streak_fruit = fruits[r]
                    # print(f"Current streak fruit: {curr_streak_fruit}")
                    curr_streak_start_ix = r
                    # print(f"Current streak start index: {curr_streak_start_ix}")
                max_len = max(max_len, r - l + 1)
                # print(f"Maximum basket collected: {max_len}")
            # when do you stop?
            if fruits[r] not in fruits_seen and len(fruits_seen) == 2:
                # print(f"This fruit {fruits[r]} is not valid in the current streak")
                # move our l to where the current streak would start
                l = curr_streak_start_ix
                # print(f"Moving our {l} such that the current baskets is now {fruits[l:r+1]}")
                # reassign fruits_seen to be the current streak fruit and the new fruit
                fruits_seen = {curr_streak_fruit, fruits[r]}
                # print(f"Reassigning our seen fruits: {fruits_seen}")
                # update the curr_streak_fruit
                # print(f"We have a new streak start!")
                curr_streak_fruit = fruits[r]
                # print(f"Current streak fruit: {curr_streak_fruit}")
                curr_streak_start_ix = r
                # print(f"Current streak start index: {curr_streak_start_ix}")
        
        return max_len
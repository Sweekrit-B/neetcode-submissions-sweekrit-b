class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for each num in nums
        # three cases
            # starting point
            # adding to the end
            # merging two consecutive sequences
        
        if len(nums) == 0:
            return 0

        consecutive_forward = {}
        backwards_attribution = {}
        visited = set()

        for num in nums:
            if num in visited:
                # print(f"Already seen {num}, skipping")
                continue
            visited.add(num)

            # currently, this number only has a consecutive sequence of one, itself
            consecutive_forward[num] = 1
            backwards_attribution[num] = num

            # first, check if we are overriding the starting point
            if num+1 in consecutive_forward:
                # grab the value of num+1 from consecutive_forward
                consecutive_forward[num] += consecutive_forward[num+1]
                # find the new endpoint of the sequence starting from num
                endpoint = num + consecutive_forward[num] - 1
                # set the backwards attribution to endpoint:num
                backwards_attribution[endpoint] = num
            
            # second, check if we are overriding an ending point
            if num-1 in consecutive_forward:
                # grab the attribution of num-1
                start = backwards_attribution[num-1]
                # create the backwards attribution
                backwards_attribution[num] = start
                # update the start value to have += how many are ahead of num
                consecutive_forward[start] += consecutive_forward[num]
                # find the new endpoint of the sequence starting from start
                endpoint = start + consecutive_forward[start] - 1
                # set the backwards attribution to endpoint:start
                backwards_attribution[endpoint] = start

            # print(f"After {num}")
            # print(f"consecutive_forward: {consecutive_forward}")
            # print(f"backwards_attribution: {backwards_attribution}")

        return max(consecutive_forward.values())

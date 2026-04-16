class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return(max(nums))

        exclude = [0, nums[1]] # exclusive array w/o first val
        include = nums[0:2] # inclusive array w/ first val
        max_e = 0 # maximum of the exclusive array
        max_i = 0 # maximum of the inclusive array
        unallowed = 0 # index of the first unallowed item in sum array (enforces 2 adj houses rule)
        
        for i in range(2, len(nums)):
            unallowed += 1 # increase the amount of allowed objects
            max_e = max(max_e, exclude[unallowed - 1]) # max of the current max and new object
            max_i = max(max_i, include[unallowed - 1]) # same logic
            exclude.append(max_e + nums[i]) # add to array w/o first two
            include.append(max_i + nums[i]) # add to array w/ first two
        
        final_sums = include[:-1] + exclude[-1:] # all but the last 
        return max(final_sums)
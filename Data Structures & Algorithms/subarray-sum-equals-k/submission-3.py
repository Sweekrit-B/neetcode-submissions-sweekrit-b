class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # intuition
        # we are essentially trying to find two prefix sums such that ps2 - ps1 = k => ps2 - k = ps1
        # what this means is that if we get a prefix sum, if it has already appeared previously, then we can add it
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        curr_prefix = 0
        res = 0
        for num in nums:
            curr_prefix += num
            # print(f"Current prefix: {curr_prefix}")
            res += prefixes[curr_prefix - k]
            # print(f"Result: {res}")
            prefixes[curr_prefix] += 1
            # print(f"Prefixes: {prefixes}")
        return res
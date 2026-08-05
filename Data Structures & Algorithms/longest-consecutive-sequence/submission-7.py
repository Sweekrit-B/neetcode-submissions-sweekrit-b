class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # neetcode
        # 0) define data structure for all sequences
        sequences = {}
        # 1) find all start sequences
        set_nums = set(nums)
        for num in set_nums:
            if num-1 not in set_nums:
                sequences[num] = 0
        # 2) for all start sequences, iterate forward
        for start in sequences:
            curr_val = start
            while curr_val in set_nums:
                sequences[start] += 1
                curr_val += 1
        
        if not sequences:
            return 0

        return max(sequences.values())

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dict of the frequency
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        # sort the dict keys by dict values
        sorted_by_freq = sorted(list(freq_dict.keys()), key = lambda number: (-freq_dict[number], number))
        return sorted_by_freq[:k]
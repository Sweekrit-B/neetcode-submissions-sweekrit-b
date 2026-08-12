class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # less efficient O(26 * n) solution

        # AABBCDEAEEEB, k = 2, answer should be 6
            # AA -> {A: 2} -> currMax = 2, currLen = 2, NoR = 0
            # AABB -> {A: 2, B: 2} -> currMax = 2, currLen = 4, NoR = 2
            # AABBC -> {A: 2, B: 2, C: 1} -> currMax = 2, currLen = 5, NoR = 3
                # ABBC -> {A: 1, B: 2, C: 1} -> currMax = 2, currLen = 4, NoR = 2
            # ABBCD -> {A: 1, B: 2, C: 1, D: 1} -> currMax = 2, currLen = 5, NoR = 3
                # BBCD -> {B: 2, C: 1, D: 1} -> currMax = 2, currLen = 4, NoR = 2
            # BBCDE -> {B: 2, C: 1, D: 1, E: 1} -> currMax = 2, currLen = 5, NoR = 3
                # BCDE -> {B: 1, C: 1, D: 1, E: 1} -> currMax = 1, currLen = 4, NoR = 3
                # CDE -> {C: 1, D: 1, E: 1} -> currMax = 1, currLen = 3, NoR = 2
            # ...

        l, r = 0, 0
        maxLen = 0
        ch_hash = defaultdict(int)

        while r < len(s):
            ch_hash[s[r]] += 1
            while (r - l + 1) - max(ch_hash.values()) > k:
                ch_hash[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            # at the end, always move r forward
            r += 1
        return maxLen

        
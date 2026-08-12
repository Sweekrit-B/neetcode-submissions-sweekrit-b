class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap solution
        charIndex = {}
        l = 0 
        res = 0

        for r in range(len(s)):
            if s[r] in charIndex and charIndex[s[r]] >= l:
                l = charIndex[s[r]] + 1
            charIndex[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
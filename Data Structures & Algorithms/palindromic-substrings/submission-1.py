class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num_counted = 0

        def countOddSubstrings(i):
            currCount = 1
            valsOut = 1
            while ((i - valsOut) >= 0) and ((i + valsOut) < n) and (s[i - valsOut] == s[i + valsOut]):
                currCount += 1
                valsOut += 1
            return currCount

        def countEvenSubstrings(i):
            if (i >= n-1) or (s[i] != s[i + 1]):
                return 0
            currCount = 1
            valsOut = 1
            while ((i - valsOut) >= 0) and ((i + valsOut + 1) < n) and (s[i - valsOut] == s[i + valsOut + 1]):
                currCount += 1
                valsOut += 1
            return currCount
        
        for i in range(len(s)):
            num_counted += countOddSubstrings(i) + countEvenSubstrings(i)
        
        return num_counted
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # neetcode-based solution
        hmp = {}
        l = 0
        maxLen = 0

        for r in range(len(fruits)):
            # default: add the fruit and move r forward
            hmp[fruits[r]] = 1 + hmp.get(fruits[r], 0)
            # while adding the fruit creates an invalid subarray
            while len(hmp) > 2:
                # remove the current l fruit
                hmp[fruits[l]] -= 1
                if hmp[fruits[l]] == 0:
                    del hmp[fruits[l]] # delete value so we can continue to use the list
                l += 1
            # after everything, the maximum length can be calculated
            maxLen = max(maxLen, sum(hmp.values()))
        
        return maxLen
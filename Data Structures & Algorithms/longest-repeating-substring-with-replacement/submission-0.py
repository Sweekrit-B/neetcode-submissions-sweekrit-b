class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # write some test cases
            # XYYX, k = 2
            # AAABABB, k = 1
            # AAABABBBB, k = 1
        # return the length of the longest substring with only one character AFTER k replacements
        # AAABABBBB is the breaking case
            # AAAB (CHANGE) AB --> length = 5
            # BA (CHANGE) BBBB --> length = 6
        
        # idea 1: check for every letter
            # essentially, initialize l and r
                # letter to use = s[l]
                # while r is not at the end of the string and num of different characters <= k
                    # move r forward
                    # also mark down the FIRST different character (d)
                # calculate the max length
                # move m to the FIRST different character (d)
            # time complexity - in the worst case, you are checking a length of m for every n characters
                # O(nm) time complexity -> not the best
        
        # idea 2: using frequency
            # lets start by just going through and recording ch repetition, k = 1
            # ideally, you are always replacing everything with
                # AAA -> {A: 3}
                # AAAB -> {A: 3, B: 1}
                # AAABA -> {A: 4, B: 1} -> NoR = 1
                # AAABAB -> {A: 4, B: 2} -> NoR = 2
                    # AABAB -> {A: 3, B: 2} -> NoR = 2
                    # ABAB -> {A: 2, B: 2} -> NoR = 2
                    # BAB -> {B: 2, A: 1} -> NoR = 1
                # BABB -> {B: 3, A: 1} -> NoR = 1...BABBBB -> {B: 5, A: 1} -> NoR = 1
            # another, more complex example
                # AABBCDEAEEEB, k = 2, answer should be 6
                # AA -> {A: 2} -> currMax = 2, currLen = 2, NoR = 0
                # AABB -> {A: 2, B: 2} -> currMax = 2, currLen = 4, NoR = 2
                # AABBC -> {A: 2, B: 2, C: 1} -> currMax = 2, currLen = 5, NoR = 3
                    # ABBC -> {A: 1, B: 2, C: 1} -> currMax = 2, currLen = 4, NoR = 2
                # ABBCD -> {A: 1, B: 2, C: 1, D: 1} -> currMax = 2, currLen = 5, NoR = 3
                    # BBCD -> {B: 2, C: 1, D: 1} -> currMax = 2, currLen = 4, NoR = 2
                # BBCDE -> {B: 2, C: 1, D: 1, E: 1} -> currMax = 2, currLen = 5, NoR = 3
                    # BCDE -> {B: 1, C: 1, D: 1, E: 1} -> currMax = 2, currLen = 4, NoR = 2
                # BCDEA -> {B: 1, C: 1, D: 1, E: 1, A: 1} -> currMax = 2, currLen = 5, NoR = 3
                    # CDEA -> {C: 1, D: 1, E: 1, A: 1} -> currMax = 2, currLen = 4, NoR = 2
                # CDEAE -> {E: 2, C: 1, D: 1, A: 1} -> currMax = 2, currLen = 5, NoR = 3
                    # DEAE -> {E: 2, D: 1, A: 1} -> currMax = 2, currLen = 4, NoR = 2
                # DEAEE -> {E: 3, D: 1, A: 1} -> currMax = 3, currLen = 5, NoR = 2
                # DEAEEE -> {E: 4, D: 1, A: 1} -> currMax = 4, currLen = 6, NoR = 2

            # some notes here:
                # we don't need to recalculate the currMax each time
                # this is because if the max at a point is not greater than currMax, then the length cannot be greater than currLen
                # this is because maxLen = currMax + k, where currMax is essentially tracking the most amount of the same character in a row
                # essentially, if we wanted to be more accurate, we COULD, but we would just be decrement from the start, which would happen at the last step anyway
        
        # pattern: since we are essentially doing a sliding window, we don't need to keep track of the actual letters, just the left and the right pointers + a hashmap to store character counts

        l, r = 0, 0
        maxLen = 0
        currMax = 0
        ch_hash = defaultdict(int)
        while r < len(s):
            # step 1: add the current r value to our hashmap
            ch_hash[s[r]] += 1
            # step 2: check if the hash value of s[r] is greater than the max
            if ch_hash[s[r]] > currMax:
                currMax = ch_hash[s[r]]
            # step 3: calculate the current length
            currLen = r - l + 1
            # step 4: determine if the number of replacements is valid
            if currLen - currMax <= k:
                maxLen = max(currLen, maxLen)
            else:
                # while we are invalid
                while currLen - currMax > k:
                    # if the number of replacements is not valid, update the dictionary
                    ch_hash[s[l]] -= 1
                    # and iterate the left pointer forward
                    l += 1
                    # and recalculate the length
                    currLen = r - l + 1
            # at the end, always move r forward
            r += 1
        return maxLen

        # dry run: "AAABABB"
        # l = 0, r = 0, mL = 0, cM = 0, hash = {}
        # iteration 1:
            # r = 1
                # hash = {A: 1}
                # 1 > 0 -> cM = 1
                # cL = 1, 1 > 0 -> mL = 1
            # r = 2
                # hash = {A: 2}
                # 2 > 1 -> cM = 2
                # cL = 2, 2 > 1 -> mL = 2
            # r = 3
                # hash = {A: 3}
                # 3 > 2 -> cM = 3
                # cL = 3, 3 > 2 -> mL = 3
            # r = 4
                # hash = {A: 3, B: 1}
                # cM = 3
                # cL = 4, 4 - 3 = 1, 4 > 3 -> mL = 4
            # r = 5
                # hash = {A: 4, B: 1}
                # 4 > 3 -> cM = 4
                # cL = 5, 5 - 4 = 1, 5 > 4 -> mL = 5
            # r = 6
                # hash = {A: 4, B: 2}
                # cM = 4
                # cL = 6, 6 - 4 = 2
                    # since 2 > 1 -> {A: 3, B: 2} is the new hash
                    # l = 1
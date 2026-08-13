class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        chs_remaining = Counter(t)
        chs_set = set(t)
        l, r = 0, 0
        curr_substr = ""

        min_len = float('inf')
        best_substr = ""
        best_l, best_r = None, None
        
        need = len(t) # how many characters do we need
        seen = 0 # how many characters have we seen
        i = 1

        while l < len(s) and r < len(s): # while the left pointer still has not hit the end yet
            # while we still need characters and the right pointer is not end
            while need != seen and r < len(s):
                # step 1: check if the current character is one that we need
                if s[r] in chs_set and chs_remaining[s[r]] > 0:
                    # step 2: if we need this character, then increment seen
                    seen += 1
                # step 3: decrement this value from chs_remaining, regardless
                chs_remaining[s[r]] -= 1
                # step 4: increment r forward (& add to current substring)
                # curr_substr += s[r]
                r += 1
                # step 5: update the best values
                if need == seen: 
                    # print("CORRECT")
                    if (r - l) < min_len:
                        min_len = r - l
                        best_l, best_r = l, r
                        # best_substr = curr_substr
                        # print("BETTER")
                # print(curr_substr)
            
            # eventually, we will get to a point where need == seen, and we need to decrement
            while need == seen and l < r:
                # step 1: check if the current character is one that we need - this means that its current val is 0
                if s[l] in chs_set and chs_remaining[s[l]] == 0:
                    # step 2: if we need this character, then decrement seen
                    seen -= 1
                # step 3: increment this value from chs_remaining, regardless
                chs_remaining[s[l]] += 1
                # step 4: increment l forward (& remove from current substring)
                # curr_substr = curr_substr[1:]
                l += 1
                # step 5: update the best values
                if need == seen: 
                    # print("CORRECT")
                    if (r - l) < min_len:
                        min_len = r - l
                        best_l, best_r = l, r
                        # best_substr = curr_substr
                        # print("BETTER")
                # print(curr_substr)
        
        if best_l is None:
            return ""
        return s[best_l:best_r]
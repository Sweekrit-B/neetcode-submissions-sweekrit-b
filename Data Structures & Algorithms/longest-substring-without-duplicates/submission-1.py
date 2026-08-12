class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window with variable length
        # initialize our initial sliding window and initial set
        # when we get a new value
            # if the new value has already been seen in the "seen" set:
                # remove from the start of our sliding window until we get to the "seen" value
            # otherwise
                # add the new val to our sliding window
            # compare the lengths each time
        
        seen = set()
        currWin = deque()
        currLen = 0
        maxLen = 0
        for ch in s:
            # if we have already seen this character
            if ch in seen:
                # remove everything before the curr character
                while currWin[0] != ch:
                    seen.remove(currWin[0])
                    currWin.popleft()
                    currLen -= 1
                # remove the repeated character
                currWin.popleft()
                currLen -= 1
                seen.remove(ch)
            # for every single character addition
            currWin.append(ch)
            currLen += 1
            seen.add(ch)
            maxLen = max(maxLen, currLen)
        
        return maxLen
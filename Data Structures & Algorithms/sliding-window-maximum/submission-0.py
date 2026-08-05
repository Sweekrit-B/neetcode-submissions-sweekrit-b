class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        currWindow = deque(nums[:k])
        maxes = [max(currWindow)]
        r = k

        while r < len(nums):
            # first, form the new window
            currWindow.popleft()
            currWindow.append(nums[r])
            # then, append the max value
            maxes.append(max(currWindow))
            # finally, iterate r forward
            r += 1
        
        return maxes
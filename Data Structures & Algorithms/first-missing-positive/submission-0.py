class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # observation
            # n belongs to the set [1, ..., len(A)+1]
        
        # method - use the input array as memory/hash set
        # we know the solution is between 1...len(A)+1 -> we have an index in the array for all values between 1...len(A) -> each value has a position in the input array
        # first,  go through the array once and turn all neg values to 0
        # as you go through the array, turn the value at the index of the current value to be negative to note that you visited it
            # if you find a 0, make it -(len(A) + 1) because that's guaranteed to be out of bounds
        # at the end, whichever index is not negative or zero

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1

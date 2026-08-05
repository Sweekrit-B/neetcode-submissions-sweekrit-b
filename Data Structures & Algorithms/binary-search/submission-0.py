class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l != r:
            if nums[(l + r)//2] < target:
                l = (l + r)//2 + 1
            elif nums[(l + r)//2] > target:
                r = (l + r)//2
            elif nums[(l + r)//2] == target:
                return (l + r)//2
        return -1
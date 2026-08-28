class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorting with a custom comparator
        arr = sorted(arr, key=lambda val: (abs(val - x), val))
        return sorted(arr[:k])
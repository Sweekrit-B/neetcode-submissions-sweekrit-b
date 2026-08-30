import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quick sort
            # develop a partition, anything less than the partition is to the left adn anything greater than the partition is to the right

        def partition(arr, low, high):
            rand_idx = random.randint(low, high)
            arr[rand_idx], arr[high] = arr[high], arr[rand_idx] # switch high and random index
            pivot = arr[high]
            i = low - 1 # start at the index before

            # traverse arr[low...high] and move all smaller elements to the left
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quickSort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)
        
        quickSort(nums, 0, len(nums)-1)
        return nums
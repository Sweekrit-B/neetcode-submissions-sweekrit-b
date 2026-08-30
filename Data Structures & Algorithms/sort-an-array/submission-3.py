class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def merge(arr, left, mid, right):
            # find the lengths of the two portions of the arrays
            n1 = mid - left + 1
            n2 = right - mid

            # create temporary arrays
            L = [0] * n1
            R = [0] * n2

            # copy data to temp arrays
            for i in range(n1):
                L[i] = arr[left + i]
            for j in range(n2):
                R[j] = arr[mid + 1 + j]
            
            i = 0
            j = 0
            k = left

            # merge the temp arrays
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            # copy the remaining elements
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1
        
        def mergeSort(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid + 1, right)
                merge(arr, left, mid, right)
        
        mergeSort(nums, 0, len(nums)-1)
        return nums
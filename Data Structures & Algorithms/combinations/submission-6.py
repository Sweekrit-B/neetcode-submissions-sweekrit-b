class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        curr_list = []
        def recurse():
            if len(curr_list) == k:
                res.append(curr_list[:])
                return
            for num in range(curr_list[-1]+1 if curr_list else 1, n+1):
                curr_list.append(num)
                recurse()
                curr_list.pop()
            return
        recurse()
        return res

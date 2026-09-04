class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        set_n = set([i for i in range(1, n+1)])
        curr_list = []
        def recurse():
            if len(curr_list) == k:
                res.append(curr_list[:])
                return
            for num in set_n:
                if not curr_list or num > curr_list[-1]:
                    curr_list.append(num)
                    recurse()
                    curr_list.pop()
            return
        recurse()
        return res

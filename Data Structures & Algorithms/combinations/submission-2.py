class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = set()
        set_n = set([i for i in range(1, n+1)])
        curr_tup = set()
        def recurse():
            if len(curr_tup) == k:
                res.add(tuple(curr_tup))
                return
            for num in set_n:
                if num not in curr_tup and (not curr_tup or num > max(curr_tup)):
                    curr_tup.add(num)
                    recurse()
                    curr_tup.remove(num)
            return
        recurse()
        return [list(r) for r in res]

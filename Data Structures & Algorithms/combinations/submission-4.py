class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = set()
        set_n = set([i for i in range(1, n+1)])
        curr_tup = []
        def recurse():
            if len(curr_tup) == k:
                res.add(tuple(curr_tup))
                return
            for num in set_n:
                if not curr_tup or num > curr_tup[-1]:
                    curr_tup.append(num)
                    recurse()
                    curr_tup.pop()
            return
        recurse()
        return [list(r) for r in res]

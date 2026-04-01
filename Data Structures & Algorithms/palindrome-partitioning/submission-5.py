class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # neetcode solution
        # for each layer, check if splitting at a certain index produces a palindrome
        # if yes, find all other potential palindromes

        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        res = []
        part = []

        def dfs(i):
            # base case -> once index has gone out of range
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)): # look for more partitions
                if is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res

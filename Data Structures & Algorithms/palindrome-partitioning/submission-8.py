class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        res = []
        part = []

        def dfs(i):
            if i >= len(s): # base case - index is out of range
                res.append(part.copy())
                return
            for j in range(i, len(s)): # for every other value
                if is_palindrome(s, i, j):
                    part.append(s[i:j+1]) # append the palindromic sequence
                    dfs(j+1) # run DFS on the next section
                    part.pop() # remove the section
        
        dfs(0)
        return res
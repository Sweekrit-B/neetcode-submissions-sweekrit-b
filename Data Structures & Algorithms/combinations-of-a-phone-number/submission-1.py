class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_dict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res = []
        curr = ""
        def dfs(i):
            nonlocal curr

            if i >= len(digits): # base case
                res.append(curr)
                return
            for ch in digits_dict[digits[i]]:
                curr += ch # add the character
                dfs(i + 1) # run DFS
                curr = curr[:-1] # remove the character
        dfs(0)
        return res

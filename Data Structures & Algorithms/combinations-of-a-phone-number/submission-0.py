class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: return []
        
        associations = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        combos = []

        def dfs(curr_index, curr_string):
            # base case
            if curr_index == len(digits):
                combos.append(curr_string)
                return
            for letter in associations[int(digits[curr_index])]:
                dfs(curr_index + 1, curr_string + letter)
        
        dfs(0, "")

        return combos
            
        
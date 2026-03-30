class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # should create a set of "allowed" values
        # initially consists of only n open parentheses
        # dfs algorithm that adds an open / close parenthesis depending on allowed options
        # if open parenthesis is added, one closed parenthesis is added to the options

        final_parens = []
        
        def dfs(curr_string, allowed_open_parens, allowed_closed_parens):
            # print("Curr string: ", curr_string)
            # print("Allowed open parentheses: ", allowed_open_parens)
            # print("Allowed closed parentheses: ", allowed_closed_parens)
            if allowed_open_parens == 0 and allowed_closed_parens == 0:
                final_parens.append(curr_string)
            if allowed_open_parens > 0:
                dfs(curr_string + "(", allowed_open_parens - 1, allowed_closed_parens + 1)
            if allowed_closed_parens > 0:
                dfs(curr_string + ")", allowed_open_parens, allowed_closed_parens - 1)
        
        dfs("", n, 0)
        
        # print(final_parens)
        return final_parens

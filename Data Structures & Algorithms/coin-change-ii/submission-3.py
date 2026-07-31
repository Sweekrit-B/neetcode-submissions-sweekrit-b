# DP - row based

class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        top_row = [0] * (amount + 1)
        top_row[-1] = 1
        bottom_row= top_row.copy()
        top_row_ix = 0

        while top_row_ix < len(coins):
            for amt_ix in range(len(top_row) - 1, -1, -1):
                coin = coins[top_row_ix]
                use_coin = top_row[amt_ix + coin] if (amt_ix + coin) < len(top_row) else 0
                top_row[amt_ix] = use_coin + bottom_row[amt_ix]
            bottom_row = top_row.copy()
            top_row_ix += 1
        
        return top_row[0]
# DP Solution - col based

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp_arr = [[0] * (amount + 1) for _ in range(len(coins))]
        for row in dp_arr:
            row[-1] = 1
        for col_ix in range(len(dp_arr[0]) - 2, -1, -1):
            for row_ix in range(len(dp_arr) - 1, -1, -1):
                # ways to get the same sum from a different coin (same level in a tree)
                val_down = dp_arr[row_ix + 1][col_ix] if (row_ix < len(dp_arr) - 1) else 0
                # ways to get the same sum if you used the current coin (deeper level in a tree)
                val_right = dp_arr[row_ix][col_ix + coins[row_ix]] if ((col_ix + coins[row_ix]) < len(dp_arr[0])) else 0
                # total sum
                dp_arr[row_ix][col_ix] = val_down + val_right
                # print(dp_arr)
            # print(dp_arr)

        return dp_arr[0][0]
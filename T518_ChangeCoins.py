from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins = [0] + coins
        dp = [[0 for _ in range(n + 1)] for _ in range(amount + 1)]
        dp[0] = [1 for _ in range(n + 1)]
        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                if i - coins[j] >= 0:
                    dp[i][j] = dp[i - coins[j]][j] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


s = Solution()
print(s.change(5, [1,2,5]))
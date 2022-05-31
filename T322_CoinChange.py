from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def inner(coins , amount):
            if amount == 0:
                memo[amount] = 0
                return 0
            if amount < 0 :
                memo[amount] = -1
                return -1
            array = []
            for coinVal in coins:
                resVal = amount - coinVal
                if resVal in memo:
                    val = memo[resVal]
                else:
                    val = inner(coins, resVal)
                if val != -1:
                    array.append(val + 1)
            if len(array) == 0:
                memo[amount] = -1
                return -1
            else:
                ans = min(array)
                memo[amount] = ans
                return ans
        return inner(coins, amount)

s = Solution()
print(s.coinChange([1], 2))

# 1092 ms, 在所有 Python3 提交中击败了74.50% 的用户
# 46.8 MB, 在所有 Python3 提交中击败了5.04% 的用户


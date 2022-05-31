from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        ans = 0
        for price in prices:
            profit = price - minPrice
            if profit > ans:
                ans = profit
            if price < minPrice:
                minPrice = price
        return ans

s = Solution()
print(s.maxProfit([7,6,4,3,1]))



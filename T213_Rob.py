from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRanges(nums: List[int]):
            sz = len(nums)
            if sz == 0:
                return 0
            if sz == 1:
                return nums[0]
            dpMaxVal = [0 for _ in range(sz)]
            for i in range(sz):
                curMax = nums[i]
                for j in range( i - 1):
                    curMax = max(dpMaxVal[j] + nums[i], curMax)
                dpMaxVal[i] = curMax
            return max(dpMaxVal[-1], dpMaxVal[-2])
        if len(nums) == 1:
            return nums[0]
        return max(robRanges(nums[:-1]), robRanges(nums[1:]))


s = Solution()
print(s.rob([1]))

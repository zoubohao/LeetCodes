from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        sz = len(nums)
        dpArray = [0 for _ in range(sz)]
        for i in range(sz):
            curMax = nums[i]
            for j in range(i - 1):
                curMax = max(curMax, dpArray[j] + nums[i])
            dpArray[i] = curMax
        return max(dpArray[-1], dpArray[-2])

s = Solution()
print(s.rob([1,2,3,1]))


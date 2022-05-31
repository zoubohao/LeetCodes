from typing import List

### dp array

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dpArray = [0  for _ in range(n)]
        ans = nums[0]
        dpArray[0] = nums[0]
        for i in range(1, n):
            dpArray[i] = max(dpArray[i - 1] + nums[i], nums[i])
            if dpArray[i] > ans:
                ans = dpArray[i]
        return ans



s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))
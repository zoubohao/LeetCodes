from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curMaxIndex = 0
        for i in range(n):
            if i <= curMaxIndex:
                if i + nums[i] > curMaxIndex:
                    curMaxIndex = i + nums[i]
            else:
                return False
        return True


s = Solution()
nums = [1,3,1,2,0,1]
print(s.canJump(nums))



from typing import List


class Solution:

    def canPartitionRec(self, nums: List[int]) -> bool:
        sumNum = sum(nums)
        if sumNum % 2 == 1: return False
        target = sumNum // 2

        def inner(nums, target):
            if len(nums) == 1:
                if nums[0] == target: return True
                else: return False
            return inner(nums[1:], target) or inner(nums[1:], target - nums[0])

        return inner(nums, target)


    def canPartitionDP(self, nums: List[int]) -> bool:
        sumNum = sum(nums)
        if sumNum % 2 == 1: return False
        target = sumNum // 2 + 1
        n = len(nums)
        dpMatrix = [[False for _ in range(n)] for _ in range(target)]

        for i in range(n):
            dpMatrix[0][i] = True

        for i in range(1, target):
            for j in range(n):
                if i == nums[j]:
                    dpMatrix[i][j] = True
                    continue
                if j - 1 < 0: continue
                if i - nums[j] >= 0:
                    dpMatrix[i][j] = dpMatrix[i - nums[j]][j - 1] or \
                        dpMatrix[i][j - 1]
                else: dpMatrix[i][j] = dpMatrix[i][j - 1]


        return dpMatrix[-1][-1]


nums = [1 ,2, 3, 6]
s = Solution()
print(s.canPartitionDP(nums))
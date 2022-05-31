from typing import List
from typing import Set

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        sortedNums = sorted(nums)

        def twoSum(nums: List[int], target: int) -> Set:
            left = 0
            right = len(nums) - 1
            ans = set()
            if len(nums) < 2: return ans
            while left < right:
                sumNum = nums[left] + nums[right]
                if sumNum == target:
                    ans.add(tuple(sorted([nums[left], nums[right]])))
                    left += 1
                    right -= 1
                elif sumNum < target:
                    left += 1
                elif sumNum > target:
                    right -= 1
            return ans

        finalAns = set()
        for i in range(len(nums)):
            curNum = sortedNums[i]
            curTwoAns = twoSum(sortedNums[i+1:], 0 - curNum)
            if len(curTwoAns) != 0:
                for twoAns in curTwoAns:
                    finalAns.add(tuple(sorted((curNum, twoAns[0], twoAns[1]))))
        ans = []
        for t in finalAns:
            ans.append(list(t))
        return ans

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))








from typing import List
from copy import deepcopy

class Solution:

    def __init__(self):
        self.count = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def backTrack(curPath: List[int], curPos: int) :
            if curPos == n:
                if target == sum(curPath):
                    self.count += 1
            else:
                for ele in ["+", "-"]:
                    if ele == "+":
                        curPath.append(nums[curPos])
                    else:
                        curPath.append(-nums[curPos])
                    backTrack(curPath, curPos + 1)
                    curPath.pop()
        backTrack([], 0)
        return self.count

nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s = Solution()
print(s.findTargetSumWays(nums, 0))

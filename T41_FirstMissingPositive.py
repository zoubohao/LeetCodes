
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        vals = []
        for ele in nums:
            if ele > 0:
                vals.append(ele)
        if len(vals) == 0: return 1
        minVal = min(vals)
        maxVal = max(vals)
        valSet = set(vals)
        if minVal == 1:
            for i in range(minVal, maxVal + 1):
                if i not in valSet:
                    return i
            return maxVal + 1
        else:
            return 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([7,8,9,11,12]))
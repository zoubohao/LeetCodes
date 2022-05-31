from typing import List
from copy import deepcopy

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def inner(selections: List[int], curArr: List[int]):
            if len(selections) == 0:
                ans.append(deepcopy(curArr))
            for ele in selections:
                curArr.append(ele)
                copySelections = deepcopy(selections)
                copySelections.remove(ele)
                inner(copySelections, curArr)
                curArr.pop()
        inner(nums, [])
        return ans


s = Solution()
print(s.permute([1,2,3]))




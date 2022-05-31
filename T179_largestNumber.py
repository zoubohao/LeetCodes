from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        comp = lambda x, y: 1 if x + y > y + x else 0
        def inner(numsStrs):
            if len(numsStrs) == 0:
                return []
            if len(numsStrs) == 1:
                return numsStrs
            before = []
            after = []
            for i in range(1, len(numsStrs)):
                if comp(numsStrs[0], numsStrs[i]) == 1:
                    after.append(numsStrs[i])
                else:
                    before.append((numsStrs[i]))
            return inner(before) + [numsStrs[0]] + inner(after)
        sortedNums = inner(strs)
        return "".join(sortedNums) if sortedNums[0] != "0" else "0"


if __name__ == "__main__":
    a = [0 ,0, 0]
    s = Solution()
    print(s.largestNumber(a))
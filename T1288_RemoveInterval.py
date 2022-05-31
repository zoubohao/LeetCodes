from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ascendOrderInterval = sorted(intervals)
        sz = len(intervals)
        if sz <= 1:
            return 1
        resSz = sz
        i = 0
        j = 1
        while j < sz:
            preInterval = ascendOrderInterval[i]
            nextInterval = ascendOrderInterval[j]
            if preInterval[0] == nextInterval[0] and \
                    preInterval[1] < nextInterval[1]:
                resSz -= 1
                i = j
            elif preInterval[1] >= nextInterval[1]:
                resSz -= 1
            else:
                i = j
            j += 1
        return resSz


s = Solution()
interval = [[1,4],[3,6],[2,8]]
print(s.removeCoveredIntervals(interval))
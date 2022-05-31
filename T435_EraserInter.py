from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedInter = sorted(intervals)
        ans = 0
        i = 0
        while i < len(sortedInter) -  1:
            curInter, nextInter =  sortedInter[i], sortedInter[i + 1]
            if curInter[0] == nextInter[0]:
                if curInter[1] <= nextInter[1]:
                    sortedInter.pop(i + 1)
                else:
                    sortedInter.pop(i)
                ans += 1
            else:
                if nextInter[0] < curInter[1]:
                    if curInter[1] <= nextInter[1]:
                        sortedInter.pop(i + 1)
                    else:
                        sortedInter.pop(i)
                    ans += 1
                else:
                    i += 1
                    continue
        return ans

    def func2(self, intervals):
        ### 主要考虑右边界
        intervals.sort(key=lambda x: (x[0]))
        n = len(intervals)
        pre = intervals[0][1]
        ans = 0
        for i in range(1, n):
            if pre > intervals[i][0]:
                ans += 1
                pre = min(intervals[i][1], pre)  # 和求交集是一个思路
            elif pre <= intervals[i][0]:
                pre = intervals[i][1]
        return ans

inter = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
s = Solution()
print(s.eraseOverlapIntervals(inter))


from typing import List
import numpy as np

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:

        def inner(h: List[int]):
            lengthH = len(h)
            hSet = set(h)
            if len(hSet) == 1:
                return lengthH * h[0]
            if lengthH == 0:
                return 0
            if lengthH  == 1:
                return h[0]
            minValue = min(h)
            minIndex = h.index(minValue)
            crossArea = lengthH * minValue
            left = inner(h[0:minIndex])
            right = inner(h[minIndex + 1:])
            return max(crossArea, left, right)
        return inner(heights)

if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([0, 9]))

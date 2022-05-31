from typing import List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sz = len(nums)
        left = 0
        right = sz - 1
        sign = False
        outMid = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                sign = True
                outMid = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if sign is False:
            return [-1, -1]
        else:
            curLeft = outMid
            while curLeft - 1 >= 0 and nums[curLeft - 1] == target:
                curLeft -= 1
            curRight = outMid
            while curRight + 1 < sz  and nums[curRight + 1] == target:
                curRight += 1
            return [curLeft, curRight]

nums = [2, 2]
s = Solution()
print(s.searchRange(nums, 2))


from typing import List
import heapq as heapqObj

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapqObj.heapify(nums)
        kthLargest = heapqObj.nlargest(k, nums)
        return kthLargest[-1]

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1,5,6,4]
    print(s.findKthLargest(nums, 2))
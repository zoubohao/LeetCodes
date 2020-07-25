import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = np.sort(nums1 + nums2)
        length = len(total)
        if length % 2 == 0:
            index1 = length // 2
            index2 = index1 - 1
            return (total[index1] + total[index2]) / 2.
        else:
            return total[length // 2]

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))


from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def inner(numList: List[int]):
            n = len(numList)
            if n == 0:
                return None
            if n == 1:
                return TreeNode(numList[0])
            medium= n // 2
            root = TreeNode(numList[medium])
            root.left = inner(numList[0:medium])
            root.right = inner(numList[medium+1:])
            return root

        return inner(nums)
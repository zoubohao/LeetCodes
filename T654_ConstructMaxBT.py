from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def inner(nums: List[int]):
            sz = len(nums)
            if sz == 0:
                return None
            elif sz  == 1:
                return TreeNode(nums[0])
            maxNum = max(nums)
            curRoot = TreeNode(maxNum)
            maxIndex = None
            for i in range(sz):
                if nums[i] == maxNum:
                    maxIndex = i
                    break
            leftChild = inner(nums[0:maxIndex])
            rightChild = inner(nums[maxIndex+1:])
            curRoot.left = leftChild
            curRoot.right = rightChild
            return curRoot

        return inner(nums)


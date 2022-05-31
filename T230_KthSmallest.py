class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.curK = 0
        self.kth = None

    def mediumTraverse(self, root: TreeNode, k):
        if root is not None:
            self.mediumTraverse(root.left, k)
            self.curK += 1
            if self.curK == k:
                self.kth = root.val
                return
            self.mediumTraverse(root.right, k)


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.mediumTraverse(root, k)
        return self.kth



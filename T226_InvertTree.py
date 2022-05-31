class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        if root.left is not None or root.right is not None:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

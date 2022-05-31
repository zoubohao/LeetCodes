class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inner(root: TreeNode) -> TreeNode:
            if root.left is None and root.right is None:
                return root
            elif root.left is None and root.right is not None:
                orderRight = inner(root.right)
                root.right = orderRight
            elif root.left is not None and root.right is None:
                orderLeft = inner(root.left)
                root.right = orderLeft
            else:
                orderLeft = inner(root.left)
                orderRight = inner(root.right)
                curNode = orderLeft
                while curNode.right is not None:
                    curNode = curNode.right
                curNode.right = orderRight
                root.right = orderLeft
            root.left = None
            return root

        if root is not None:
            inner(root)
            root.left = None




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        step = 1
        queue = []
        visited = set()
        queue.append(root)
        visited.add(root)
        while len(queue) != 0:
            sz = len(queue)
            for i in range(sz):
                curNode = queue.pop(0)
                if curNode.left is None and curNode.right is None:
                    return step
                if curNode.left is not None and curNode.left not in visited:
                    queue.append(curNode.left)
                    visited.add(curNode.left)
                if curNode.right is not None and curNode.right not in visited:
                    queue.append(curNode.right)
                    visited.add(curNode.right)
            step += 1

root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(3)
root.left.left= TreeNode(4)
root.right.right = TreeNode(5)

s = Solution()
print(s.minDepth(root))





class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def connectTwoSide(node1, node2):
            if node1 is None or node2 is None:
                return
            node1.next = node2
            connectTwoSide(node1.left, node1.right)
            connectTwoSide(node2.left, node2.right)
            connectTwoSide(node1.right, node2.left)

        connectTwoSide(root.left, root.right)
        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node2ParentList = {root.val: []}
        pVal = p.val
        qVal = q.val
        def traverse(currentNode: TreeNode):
            if pVal not in node2ParentList or qVal not in node2ParentList:
                val = currentNode.val
                leftNode = currentNode.left
                rightNode = currentNode.right
                if leftNode is not None:
                    node2ParentList[leftNode.val] = [currentNode] + node2ParentList[val]
                    traverse(leftNode)
                if rightNode is not None:
                    node2ParentList[rightNode.val] = [currentNode] + node2ParentList[val]
                    traverse(rightNode)
        traverse(root)
        p_ancestors_list = node2ParentList[pVal]
        q_ancestors_list = node2ParentList[qVal]
        p_ancestors = set(node2ParentList[pVal])
        q_ancestors = set(node2ParentList[qVal])
        if p in q_ancestors: return p
        if q in p_ancestors: return q
        p_Num = len(p_ancestors)
        q_Num = len(q_ancestors)
        if p_Num < q_Num:
            for obj in p_ancestors_list:
                if obj in q_ancestors: return obj
        else:
            for obj in q_ancestors_list:
                if obj in p_ancestors: return obj

if __name__ == "__main__":
    # root = TreeNode(3)
    # p = root.left = TreeNode(5)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(6)
    # root.left.right = TreeNode(2)
    # root.left.right.left = TreeNode(7)
    # q = root.left.right.right = TreeNode(4)
    # root.right.left = TreeNode(0)
    # root.right.right = TreeNode(8)
    # root.right.right.right = TreeNode(10)
    # root = TreeNode(9)
    # root.left = TreeNode(-1)
    # root.right = TreeNode(-4)
    # root.left.left = TreeNode(10)
    # p =root.left.right = TreeNode(3)
    # q = root.left.left.right = TreeNode(5)
    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-2)
    q = root.left.right = TreeNode(4)
    p = root.left.left.left = TreeNode(8)

    s = Solution()
    print(s.lowestCommonAncestor(root, p, q).val)







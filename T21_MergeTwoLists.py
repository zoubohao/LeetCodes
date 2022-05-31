

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 is None and l2 is None: return None
        elif l1 is None: return l2
        elif l2 is None: return l1
        else:
            curL1 = l1
            curL2 = l2
            fakeRoot = curNode = ListNode(0)
            while curL1 is not None and curL2 is not None:
                if curL1.val < curL2.val:
                    curL1Next = curL1.next
                    curNode.next = curL1
                    curL1 = curL1Next
                else:
                    curL2Next = curL2.next
                    curNode.next = curL2
                    curL2 = curL2Next
                curNode = curNode.next
            if curL1 is not None: curNode.next = curL1
            else: curNode.next = curL2
            return fakeRoot.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(4)
    n2 = ListNode(1)
    n2.next = ListNode(3)
    n2.next.next = ListNode(4)

    s = Solution()
    root = s.mergeTwoLists(n1, n2)
    while root is not None:
        print(root.val)
        root = root.next




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentL1String = ""
        currentL2String = ""
        while l1.next is not None:
            currentL1String = str(l1.val) + currentL1String
            l1 = l1.next
        currentL1String = str(l1.val) + currentL1String
        while l2.next is not None:
            currentL2String = str(l2.val) + currentL2String
            l2 = l2.next
        currentL2String = str(l2.val) + currentL2String
        v1 = int(currentL1String)
        v2 = int(currentL2String)
        vs = str(v1 + v2)
        resultList = None
        nextNode = ListNode()
        for i in range(len(vs)-1, -1, -1):
            if i == (len(vs)-1):
                resultList = nextNode
            if i != 0:
                nextNode.val = vs[i]
                nextNextNode = ListNode()
                nextNode.next = nextNextNode
                nextNode = nextNextNode
            else:
                nextNode.val = vs[i]
        return resultList

if __name__ == "__main__":
    l1_2 = ListNode(2)
    l1_4 = ListNode(4)
    l1_3 = ListNode(3)
    l1_4.next = l1_3
    l1_2.next = l1_4

    l2_5 = ListNode(5)
    l2_6 = ListNode(6)
    l2_4 = ListNode(4)
    l2_6.next = l2_4
    l2_5.next = l2_6

    so = Solution()
    r = so.addTwoNumbers(l1_2,l2_5)
    c = ""
    while r.next is not None:
        c = str(r.val) + c
        r = r.next
    c = str(r.val) + c
    print(c)





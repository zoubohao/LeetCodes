from typing import  List

class Solution:

    def adjNodeGenerate(self, deadends: List[str], curNode: str):

        def plusOne(curNode, i):
            curList = list(curNode)
            if curList[i] == "9":
                curList[i] = "0"
            else:
                curNum = int(curList[i])
                curNum += 1
                curList[i] = str(curNum)
            return "".join(curList)

        def minusOne(curNode, i):
            curList = list(curNode)
            if curList[i] == "0":
                curList[i] = "9"
            else:
                curNum = int(curList[i])
                curNum -= 1
                curList[i] = str(curNum)
            return "".join(curList)

        outNodes = []
        for i in range(4):
            p_i = plusOne(curNode, i)
            m_i = minusOne(curNode, i)
            if p_i not in deadends:
                outNodes.append(p_i)
            if m_i not in deadends:
                outNodes.append(m_i)
        return outNodes


    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        visited = set()
        if "0000" in deadends:
            return -1
        queue.append("0000")
        visited.add("0000")
        step = 0
        while len(queue) != 0:
            print(queue)
            sz = len(queue)
            for _ in range(sz):
                curNode = queue.pop(0)
                if curNode == target:
                    return step
                nextNodes = self.adjNodeGenerate(deadends, curNode)
                for node in nextNodes:
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)
            step += 1
        return -1

deadends = [""]
s = Solution()
print(s.openLock(deadends, "8888"))
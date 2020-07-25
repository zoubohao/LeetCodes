import numpy as np

class Solution:
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        charInZ = 3 * numRows - 2
        behand = 2 * numRows - 2
        left = len(s) - charInZ
        count = left // behand + 1
        cols = numRows + count * (numRows - 1)
        positionMatrix = [["" for _ in range(cols)] for _ in range(numRows)]
        positionMatrix = np.array(positionMatrix)
        r, c = 0, 0
        for i, s in enumerate(s):
            sign = True
            positionMatrix[r, c] = s
            if r == (numRows - 1):
                c += 1
                r -= 1
                sign = False
            if sign:
                if c % (numRows - 1) == 0:
                    r += 1
                else:
                    r -= 1
                    c += 1
        newS = ""
        for i in range(numRows):
            for j in range(cols):
                newS += positionMatrix[i, j]
        return newS



if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("",1))


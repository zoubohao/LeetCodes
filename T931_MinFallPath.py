from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dpMatrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dpMatrix[0][i] = matrix[0][i]
        ### dp processing
        for i in range(1, n):
            for j in range(n):
                fromThree = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]
                curRes = []
                for posI, posJ in fromThree:
                    if 0 <= posI < n and 0 <= posJ < n:
                        curRes.append(matrix[i][j] + dpMatrix[posI][posJ])
                dpMatrix[i][j] = min(curRes)
        return min(dpMatrix[-1])

matrix = [[-48]]
s = Solution()
print(s.minFallingPathSum(matrix))



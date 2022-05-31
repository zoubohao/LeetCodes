from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        record_grid = [[0 for _ in range(n)] for _ in range(m)]
        curSum = 0
        for j in range(n):
            curSum += grid[0][j]
            record_grid[0][j] = curSum
        curSum = 0
        for i in range(m):
            curSum += grid[i][0]
            record_grid[i][0] = curSum
        for i in range(1, m):
            for j in range(1, n):
                record_grid[i][j] = min(record_grid[i - 1][j], record_grid[i][j - 1]) + grid[i][j]
        return record_grid[-1][-1]


if __name__ == "__main__":
    s = Solution()
    grid = [[1,2,3],[4,5,6]]
    print(s.minPathSum(grid))



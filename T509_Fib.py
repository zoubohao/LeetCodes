

class Solution:

    def fib(self, n: int) -> int:
        memo = {}
        def inner(n: int) -> int:
            if n == 0: return 0
            if n == 1: return 1
            if n in memo:
                return memo[n]
            else:
                val = inner(n - 1) + inner(n - 2)
                memo[n] = val
                return val
        return inner(n)

s = Solution()
print(s.fib(4))

# 执行用时：28 ms, 在所有 Python3 提交中击败了90.06% 的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了82.45%的用户




class Solution:
    def myPow(self, x: float, n: int) -> float:
        multiNum = 1.
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n >= 0 :
            for i in range(n):
                multiNum = multiNum * x
                if multiNum == 0:
                    return 0
        else:
            for i in range(abs(n)):
                multiNum = multiNum * x
                if (1./multiNum) == 0:
                    return 0
            multiNum = 1. / multiNum
        return multiNum


if __name__ == "__main__":
    import math
    so = Solution()
    print(so.myPow(0.1, 2147483647))
    print(math.pow(2., -2147483648))
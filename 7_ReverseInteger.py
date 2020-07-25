class Solution:
    def reverse(self, x: int) -> int:
        ifNeg = False
        if x < 0 :
            ifNeg = True
        string = str(x)
        newString = ""
        if ifNeg:
            for i in range(len(string)-1, 0, -1):
                newString = newString + string[i]
            if len(newString) == 1:
                return x
            if newString[0] == 0:
                newString = newString[1:len(newString)]
            newString = "-" + newString
            newInt = int(newString)
            if newInt < -2 ** 31 :
                return 0
            return newInt
        else:
            for i in range(len(string)-1, -1, -1):
                newString = newString + string[i]
            if len(newString) == 1:
                return x
            if newString[0] == 0:
                newString = newString[1:len(newString)]
            newInt = int(newString)
            if newInt >= 2**31:
                return 0
            return newInt


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(1534236469))

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        resultList = re.findall("^" + p + "$",s)
        if len(resultList) != 0:
            return True
        else:
            return False


if __name__ == "__main__":
    so = Solution()
    print(so.isMatch("aaa", "a"))







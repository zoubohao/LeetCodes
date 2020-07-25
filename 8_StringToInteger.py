import re

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        regexNumberBegin = re.compile(r"[+\-0-9]")
        regexNumberMedi = re.compile(r"[0-9]")
        wordsBeginIndex = 0
        for i, s in enumerate(str):
            if s != " ":
                wordsBeginIndex = i
                break
        if len(regexNumberBegin.findall(str[wordsBeginIndex])) == 0:
            return 0
        newString = ""
        for i in range(wordsBeginIndex, len(str)):
            if i == wordsBeginIndex:
                if len(regexNumberBegin.findall(str[i])) == 0:
                    break
                else:
                    newString = newString + regexNumberBegin.findall(str[i])[0]
            else:
                if len(regexNumberMedi.findall(str[i])) != 0:
                    newString = newString + regexNumberMedi.findall(str[i])[0]
                else:
                    break
        try:
            intNum = int(newString)
            if intNum < - 2 ** 31:
                return -2 ** 31
            elif intNum >= 2 ** 31:
                return 2 ** 31 - 1
            else:
                return intNum
        except:
            return 0





if __name__ == "__main__":
    so = Solution()
    print(so.myAtoi("-5-"))
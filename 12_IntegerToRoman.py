class Solution:
    def intToRoman(self, num: int) -> str:
        int2RomanMap = {1 : "I", 5 : "V",
                        10: "X", 50: "L",
                        100 : "C", 500 : "D",
                        1000 : "M",
                        4: "IV", 9: "IX",
                        40: "XL", 90: "XC",
                        400: "CD", 900: "CM"
                        }
        sort = list(reversed(sorted(list(int2RomanMap.keys()))))
        record = [0 for _ in range(len(sort))]
        for i,sortNum in enumerate(sort):
            record[i] = num // sortNum
            num = num % sortNum
        newString = ""
        for i, recordNum in enumerate(record):
            newString = newString + int2RomanMap[sort[i]] * recordNum
        return newString

if __name__ == "__main__":
    so = Solution()
    print(so.intToRoman(2020))

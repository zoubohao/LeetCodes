

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Size = len(s1)
        s2Size = len(s2)
        if s2Size < s1Size:
            return False
        left = 0
        right = s1Size
        valid = 0
        need = {}
        window = {}
        for ele in s1:
            if ele in need: need[ele] += 1
            else: need[ele] = 1
        needSize = len(need)
        ### Fixed window size
        for i in range(s1Size):
            curChar = s2[i]
            if curChar not in window: window[curChar] = 1
            else: window[curChar] += 1
            if curChar in need and window[curChar] == need[curChar]:
                valid += 1
        if valid == needSize:
            return True
        while right < s2Size:
            ### add one char
            addChar = s2[right]
            if addChar in window: window[addChar] += 1
            else: window[addChar] = 1
            if addChar in need and window[addChar] == need[addChar]:
                valid += 1
            ### currently remove one char
            removeChar = s2[left]
            if removeChar in need:
                if window[removeChar] == need[removeChar]:
                    valid -= 1
                window[removeChar] -= 1
            right += 1
            left += 1
            if valid == needSize:
                return True
        return False

s = Solution()
print(s.checkInclusion("ab", "eidboaooo"))

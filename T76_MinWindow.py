

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        valid = 0
        start = 0
        length = float("inf")
        need = {}
        window = {}
        for ele in t:
            if ele in need:
                need[ele] += 1
            else:
                need[ele] = 1
        needSize = len(need)
        while right < len(s):
            addChar = s[right]
            right += 1
            ### Add to window
            if addChar not in window:
                window[addChar] = 1
            else:
                window[addChar] += 1
            ### use valid variable to record if the substring in window satisfy the needed.
            if addChar in need and window[addChar] == need[addChar]:
                valid += 1
            ### if satisfy, needs to shrink.
            while valid == needSize:
                if right - left < length:
                    start = left
                    length = right - left
                removeChar = s[left]
                left += 1
                if removeChar in need:
                    if window[removeChar] == need[removeChar]:
                        valid -= 1
                    window[removeChar] -= 1
        if length == float("inf"): return  ""
        else: return s[start: start + length]



s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))


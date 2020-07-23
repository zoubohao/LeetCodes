class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        length = len(s)
        for i, char in enumerate(s):
            if i >= (length - longest):
                break
            currentSet = set()
            currentSet.add(char)
            for j in range(i + 1, length):
                if s[j] not in currentSet:
                    currentSet.add(s[j])
                else:
                    break
            if len(currentSet) > longest:
                longest = len(currentSet)
        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(" "))

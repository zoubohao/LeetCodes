from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.trap([4,2,0,3,2,5]))
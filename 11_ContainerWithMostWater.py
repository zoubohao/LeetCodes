
class Solution:
    def maxArea(self, height: list):


        length = len(height)
        area = 0
        if height == list(sorted(height)):
            print("sorted")
            for i in range(length):
                currentArea = height[i] * abs(length - 1 - i)
                if currentArea > area:
                    area = currentArea
            return area
        if height == list(reversed(sorted(height))):
            print("reversed")
            for i in range(length - 1, -1 , -1):
                currentArea = height[i] * i
                print(currentArea)
                if currentArea > area:
                    area = currentArea
            return area
        print("Normal")
        maxHeight = max(height)
        for i in range(length):
            iHeight = height[i]
            for j in range(length - 1, i - 1, -1):
                jHeight = height[j]
                minHeight = iHeight
                if jHeight < iHeight:
                    minHeight = jHeight
                currentArea = abs(j - i) * minHeight
                if currentArea > area:
                    area = currentArea
                if (maxHeight * (j - i)) < area :
                    break
        return area


if __name__ == "__main__":
    so = Solution()
    print(so.maxArea([2,1]))







class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        maxwater = 0
        while p1<p2 :
            l = p2-p1
            b = min(height[p1],height[p2])
            area = l*b
            maxwater = max(maxwater, area)
            if height[p1] < height[p2] :
                p1+=1
            else :
                p2-=1
        return maxwater
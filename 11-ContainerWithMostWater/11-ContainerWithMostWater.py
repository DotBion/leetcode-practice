# Last updated: 6/1/2025, 9:39:26 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #n2 solution
        # max = 0
        # for i in range(len(height)-1) :
        #     for j in range(i+1,len(height)) :
        #         minh = min(height[i],height[j])
        #         breadth = j - i
        #         water = minh*breadth
        #         if water > max :
        #             max = water
        # return max
        left = 0 
        right = len(height)-1 #length is max from start
        max = 0
        while left<right:
            length = right - left
            breadth = min(height[left],height[right])
            water = length*breadth #area
            if water > max :
                max = water
            if breadth == height[left] :
                left+=1
            else :
                right-=1
        return max



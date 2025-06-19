# Last updated: 6/19/2025, 6:32:00 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0

        for i in nums :
            if i == 0 :
                red+=1
            elif i==1 :
                white+=1
            elif i==2 :
                blue+=1

        #rewrite the nums array
        for i in range(red) :
            nums[i] = 0
        for i in range(red, red+white) :
            nums[i] = 1
        for i in range(red+white, red+white+blue) :
            nums[i] = 2

        return nums
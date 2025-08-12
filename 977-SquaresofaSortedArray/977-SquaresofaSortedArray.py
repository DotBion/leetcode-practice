# Last updated: 8/11/2025, 8:41:16 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left, right = 0, l - 1
        squares = [0]*l
        for i in range(l) :
            if abs(nums[left]) < abs(nums[right]) :
                squares[l-i-1] = nums[right] ** 2
                right-=1
            else :
                squares[l-i-1] = nums[left]**2
                left+=1
        return squares
        
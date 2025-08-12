# Last updated: 8/11/2025, 8:40:25 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        squares = [0]*len(nums)
        for i in range(len(nums)) :
            if abs(nums[left]) < abs(nums[right]) :
                squares[len(nums)-i-1] = nums[right] ** 2
                right-=1
            else :
                squares[len(nums)-i-1] = nums[left]**2
                left+=1
        return squares
        
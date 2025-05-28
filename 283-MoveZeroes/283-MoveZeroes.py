# Last updated: 5/28/2025, 6:18:55 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        #move all nonzero to left or zeros to right
        for right in range(len(nums)) :
            if nums[right]!=0 :
                #if left is non-zero we just swap it with itself
                nums[right], nums[left] = nums[left], nums[right]
                left+=1
        
        
# Last updated: 9/7/2025, 10:02:34 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1 :
            return 0
        cost = 0
        for i in range(len(nums)) :
            cost += nums[i]
        leftsum = 0
        for i in range(len(nums)) :
            if leftsum == (cost - nums[i]-leftsum) :
                return i
            leftsum+=nums[i]
        return -1
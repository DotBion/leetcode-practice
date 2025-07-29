# Last updated: 7/29/2025, 5:48:11 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        ops = 0
        while left<right :
            sum = nums[left] + nums[right]
            if sum == k:
                right-=1
                left+=1
                ops+=1
            elif sum > k :
                right-=1
            elif sum < k :
                left+=1
        return ops
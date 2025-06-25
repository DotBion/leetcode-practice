# Last updated: 6/25/2025, 5:09:15 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        if l>1 :
            return nums[l//2]
        return nums[0]
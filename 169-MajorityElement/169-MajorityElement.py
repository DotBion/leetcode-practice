# Last updated: 6/25/2025, 5:09:30 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        return nums[l//2]
        #return nums[0]
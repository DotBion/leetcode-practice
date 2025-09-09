# Last updated: 9/9/2025, 8:54:24 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums_set = set(nums)
        for i in range(l+1) :
            if i not in nums_set :
                return i

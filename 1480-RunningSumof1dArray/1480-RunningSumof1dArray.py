# Last updated: 8/14/2025, 9:43:28 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = [nums[0]]
        for i in range(1,len(nums)) :
            rsum.append(rsum[i-1]+nums[i])
        return rsum
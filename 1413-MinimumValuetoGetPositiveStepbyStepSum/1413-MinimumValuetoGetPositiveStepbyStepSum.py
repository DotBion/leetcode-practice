# Last updated: 8/14/2025, 10:01:48 PM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minsum = nums[0]
        prefixsum = [nums[0]]
        for i in range(1,len(nums)) :
            temp = prefixsum[i-1]+nums[i]
            prefixsum.append(temp)
            if temp < minsum :
                minsum = temp
        if minsum < 0 :
            return 1+abs(minsum)
        return 1
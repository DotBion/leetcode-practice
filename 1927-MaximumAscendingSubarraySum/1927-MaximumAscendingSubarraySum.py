# Last updated: 7/29/2025, 5:48:07 PM
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0] 
        sum = maxSum
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                maxSum = max(sum,maxSum)
                sum = 0
                #if sum > maxSum :
                #    maxSum = sum
                #sum = nums[i]
            #else :
            sum += nums[i]
        #f sum > maxSum :
        #   maxSum = sum
        return max(maxSum,sum)
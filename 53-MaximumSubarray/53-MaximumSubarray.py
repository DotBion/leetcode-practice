# Last updated: 6/20/2025, 12:18:25 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #no point in carrying a negative sum since the sum will always reduce!
        maxSum = nums[0]
        right = 0
        sum = 0
        while right < len(nums)  :
            
            if sum < 0 :
                sum = 0
            sum+=nums[right]
            if sum>maxSum :
                maxSum = sum
            right+=1
        return maxSum


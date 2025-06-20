# Last updated: 6/20/2025, 12:19:00 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #no point in carrying a negative sum since the sum will always reduce!
        maxSum = nums[0]
        right = 0
        sum = 0
        while right < len(nums)  :    
            if sum < 0 :
                sum = 0
            sum+=nums[right] #so that sum=0 is not taken into account
            if sum>maxSum :
                maxSum = sum
            right+=1
        return maxSum


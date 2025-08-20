# Last updated: 8/20/2025, 7:39:53 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        currsum = 0
        res = float('inf')
        for right in range(len(nums)):
            currsum+=nums[right]
            while currsum >= target :
                res = min(res, right-left+1)
                currsum -= nums[left]
                left+=1
        return res if res!= float('inf') else 0



# Last updated: 8/17/2025, 10:25:42 AM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1 : #what if [0,0,0,0,1,0,0] k=1 as input ??? invalid test case lol!
            return 0
        left = 0
        curr = 1
        ans = 0
        for right in range(len(nums)) :
            curr *= nums[right]
            while curr >= k :
                curr //= nums[left]
                left+=1
            ans += right - left + 1
        return ans

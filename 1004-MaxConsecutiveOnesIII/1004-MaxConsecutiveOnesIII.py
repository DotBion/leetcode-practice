# Last updated: 8/13/2025, 5:54:06 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lo = 0
        left, right = 0,0
        for right in range(len(nums)) :
            if nums[right] == 0 :
                k-=1
            while k<0 :
                if nums[left] == 0 :
                    k+=1
                left+=1
            lo = max(lo, right-left+1)
        return lo
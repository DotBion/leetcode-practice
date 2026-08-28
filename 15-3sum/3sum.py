class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        left, right = 0, len(nums)-1
        for i in range(len(nums)-2) :
            if i>0 and nums[i]==nums[i-1] :
                continue
            right = len(nums) - 1
            left=i+1
            while left<right :
                s=nums[left]+nums[right]
                if s == -nums[i] :
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left<right :
                        left+=1
                elif s >= -nums[i] : 
                    right -= 1
                else :
                    left+=1
        return res   
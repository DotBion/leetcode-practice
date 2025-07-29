# Last updated: 7/29/2025, 5:48:42 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

            res = []
            nums.sort()
            r = len(nums)
            for i in range(len(nums)):
                if i>0 and nums[i-1] == nums[i]:
                    continue

                r = len(nums) -1 
                l = i + 1
                
                while l<r :
                    threeSum = nums[i] + nums[l] + nums[r]
                    if threeSum > 0 :
                        r-=1
                    elif threeSum < 0 :
                        l+=1
                    else :
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r :
                            l+=1
            return res
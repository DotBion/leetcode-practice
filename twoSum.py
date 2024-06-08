class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            compli = target - nums[i]
            if compli in hm :
                return [hm[compli],i]
            hm[nums[i]] = i
        return []
        
        
        
        

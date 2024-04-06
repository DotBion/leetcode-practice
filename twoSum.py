class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices=[]
        numsMap={}
        #build hash table
        for i in range(len(nums)):
            numsMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsMap and numsMap[complement]!=i:
                return [i,numsMap[complement]]

        return []

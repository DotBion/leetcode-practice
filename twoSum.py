class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices=[]
        for i in range(len(nums)-1):
            #print(i": ")
            for j in range(i+1,len(nums)):
                #print(j)
                if nums[i]+nums[j] == target:
                    indices.append(i)
                    indices.append(j)
                    break
        return indices

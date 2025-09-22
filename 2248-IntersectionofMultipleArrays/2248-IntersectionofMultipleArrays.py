# Last updated: 9/22/2025, 7:24:29 PM
from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for i in range(len(nums)) :
            for j in range(len(nums[i])) :
                #print(i,j)
                counts[nums[i][j]]+=1
        result = []
        print(counts)
        for key,value in counts.items() : #enumerate-wrong
            print(key,value)
            if value == len(nums) :
                result.append(key)

        return sorted(result)
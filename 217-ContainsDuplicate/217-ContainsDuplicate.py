# Last updated: 7/29/2025, 5:48:26 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        for i in nums:
            if i in d:
                return True
            d[i]+=1
        return False
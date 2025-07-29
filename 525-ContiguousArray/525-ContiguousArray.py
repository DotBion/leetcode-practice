# Last updated: 7/29/2025, 5:48:17 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        maxlen = 0
        mapci = {0:-1}
        for i in range(len(nums)) :
            if nums[i]==0 :
                count-=1
            elif nums[i]==1 :
                count+=1
            if count in mapci.keys() :
                maxlen = max(maxlen, i-mapci[count])
            else :
                mapci[count]=i
        return maxlen

# Last updated: 8/17/2025, 9:24:33 AM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs=[]
        l=len(nums)
        prefix = [0,nums[0]]
        for i in range(1,l) :
            prefix.append(prefix[i]+nums[i])
        print(prefix)
        for i in range(len(nums)) :
            if i-k<0 or i+k>=l :
                avgs.append(-1)
            else :
                avg = (prefix[i+k+1] - prefix[i-k])//(2*k+1)
                avgs.append(avg)
        return avgs
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 :
            return False
        target = sum(nums)//2
        dp = ([0])

        for i in range(len(nums)-1,-1,-1) :
            currdp = set(dp)
            for d in dp :
                if d+nums[i] == target :
                    return True
                currdp.add(d+nums[i])
            dp = currdp
        return False
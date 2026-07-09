# Last updated: 7/9/2026, 10:18:50 AM
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        rs = [nums[0]]
4        for i in range(1,len(nums)) :
5            rs.append(rs[i-1]+nums[i])
6        return rs
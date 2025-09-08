# Last updated: 9/8/2025, 8:13:26 AM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        prefixsum = [nums[0]]
        for i in range(1,len(nums)) :
            prefixsum.append(prefixsum[-1]+nums[i])
        self.prefixsum = prefixsum
    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right] - self.prefixsum[left] + self.nums[left]


    # def sumRange(self, left: int, right: int) -> int:
    #     s = 0
    #     for i in range(left,right+1) :
    #         s+=self.nums[i]
    #     return s
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
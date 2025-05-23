# Last updated: 5/23/2025, 7:13:26 PM
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # prev = 0
        # next = 0
        # #this considers only continuous case
        # for i in range(1,len(nums)-1) :
        #     next = i+1
        #     if nums[prev]<nums[i]<nums[next] :
        #         return True
        #     prev = i

        # return False
        first = float('inf')
        second = float('inf')
        print(type(first))
        for i in nums :
            print(type(i))
            if i <= first :
                first = i
            elif i <= second :
                second = i
            else :
                return True
        return False

# Last updated: 6/25/2025, 4:38:25 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #timeout
        # for i in range(len(nums)) :
        #     for j in range(i+1,len(nums)) :
        #         if nums[i] == nums[j]:
        #             return nums[i]
        # return False
        #take slow and fast pointer - since cycle meets at a point = NOT NECESSARILY THE DUPLICATE EL but BOTH PTRS EQUIDISTANT FROM THE DUPLICATE POINT
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow ==fast:
                break
        slow2 = nums[0]
        while slow!=slow2 :
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left<=right :
            mid = (left+right)//2
            if target == nums[mid] :
                return mid
            elif nums[left] <= nums[mid]:
                #left half is sorteed, right half is messy
                #now check for target
                if nums[left] <=target<nums[mid] :
                    #searching target on the left sorted half
                    #<=n[mid] bkz mid is already checked
                    right = mid-1
                else : 
                    #target on unsorted rh
                    left = mid + 1
            else :
                #left half is messy, right half is sorted
                if nums[mid] < target <= nums[right] :
                    #target in the sorted rh
                    left = mid + 1
                else :
                    # target in the left messy hf
                    right = mid - 1
        return -1


                



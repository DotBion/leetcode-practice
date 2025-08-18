# Last updated: 8/18/2025, 9:21:38 AM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        set1 = set(nums1)
        for num in nums2 :
            if num in set1 :
                return num
        return -1




        #TLE
        # for i in nums1 :
        #     for j in nums2 :
        #         if i == j :
        #             return i
        # return -1
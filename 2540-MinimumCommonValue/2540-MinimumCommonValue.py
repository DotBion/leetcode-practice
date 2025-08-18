# Last updated: 8/18/2025, 9:29:28 AM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = 0,0

        while l1<len(nums1) and l2<len(nums2) :
            if nums1[l1] < nums2[l2] :
                l1+=1
            elif nums1[l1] > nums2[l2] :
                l2+=1
            else :
                return nums1[l1]

        return -1 



        #O(n+m)
        # set1 = set(nums1)
        # for num in nums2 : #O(1) since hash
        #     if num in set1 :
        #         return num
        # return -1


        #TLE O(nm)
        # for i in nums1 :
        #     for j in nums2 :
        #         if i == j :
        #             return i
        # return -1
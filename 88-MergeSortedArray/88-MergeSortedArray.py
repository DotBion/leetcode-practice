# Last updated: 6/25/2025, 3:42:08 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        right = m+n-1
        while p1>=0 and p2>=0 :
            if nums1[p1] >= nums2[p2] :
                nums1[right] = nums1[p1]
                right-=1
                p1-=1
            else :
                nums1[right] = nums2[p2]
                right-=1
                p2-=1
        #print(nums1,nums2,right,p1,p2)
        while p2>=0:
            nums1[right] = nums2[p2]
            right-=1
            p2-=1
        return nums1


            
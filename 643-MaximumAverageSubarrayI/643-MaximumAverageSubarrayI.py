# Last updated: 8/13/2025, 3:30:54 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''O(n) wo cumulative sum'''
        res = sum(nums[:k])
        window_sum = res
        left, right = 1,k
        while right<len(nums) :
            window_sum += nums[right] - nums[left-1]
            res = max(res,window_sum)
            right+=1
            left+=1
        return res/k
        '''O(n)'''
        # l = len(nums)
        # for i in range(1,l) :
        #     nums[i]+=nums[i-1]
        # res = nums[k-1]
        # left = 1
        # right = k
        # while right<l :
        #     res = max(res, nums[right]-nums[left-1])
        #     left+=1
        #     right+=1
        # return res/k

        # maxAvg = float('-inf')
        # left, right = 0,0+k
        # while right<=len(nums) :
        #     avg = 0
        #     for i in range(left, right) :
        #         avg += nums[i]
        #     avg /= k
        #     if avg > maxAvg :
        #         maxAvg = avg
        #     right+=1
        #     left+=1
        # return maxAvg
                
            
            
# Last updated: 7/9/2026, 9:36:20 AM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        maxzero = left = 0
4        curr_wind_size = 0
5        for right in range(len(nums)) :
6            if nums[right] == 0 :
7                maxzero += 1
8            
9            #invalid window
10            while maxzero > k :
11                if nums[left] == 0:
12                    maxzero -= 1
13                left+=1
14            
15            curr_wind_size = max(curr_wind_size, right - left + 1)
16            
17        return curr_wind_size
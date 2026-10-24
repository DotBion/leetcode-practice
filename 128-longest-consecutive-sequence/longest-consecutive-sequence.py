class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s=set(nums)
        maxlen = 0
        for i in s:
            count = 0
            r = i
            if i-1 not in s:
                while r in s :
                    count+=1
                    r+=1
            maxlen = max(maxlen, count)
        return maxlen
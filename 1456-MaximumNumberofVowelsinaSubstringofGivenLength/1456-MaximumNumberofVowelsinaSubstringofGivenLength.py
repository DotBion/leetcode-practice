# Last updated: 9/4/2025, 11:07:07 AM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vc = 0 
        vcmax = 0
        vowels = {'a','e','i','o','u'}#faster lookup #vowels = ['a','e','i','o','u']
        left = 0
        right = k
        for i in range(left,right) :
            if s[i] in vowels :
                vc+=1
        vcmax = vc
        for i in range(right, len(s)) :
            if s[left] in vowels :
                vc-=1
            if s[i] in vowels :
                vc+=1
            left+=1
            if vc>vcmax :
                vcmax = vc
        return vcmax
            


        # vCount = 0
        # maxvc = 0
        # vowels = ['a','e','i','o','u']
        # left = 0
        # right = k 
        # while right <= len(s) :
        #     for i in range(left,right) :
        #         if s[i] in vowels :
        #             vCount +=1
        #     if vCount > maxvc :
        #         maxvc = vCount
        #     vCount = 0
        #     left+=1
        #     right+=1
        # return maxvc

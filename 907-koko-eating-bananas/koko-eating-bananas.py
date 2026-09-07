from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) #k or speed upper and lower limit
        while left<right : 
            m = (left+right)//2 #start with a mid value for K
            hours=0
            for p in piles : #calculate the total time the selected k value
                hours += ceil(p/m) #(p+m-1)//2
            if hours<=h : #works
            #we see if it still holds for a smaller value
                right = m
            else : 
                left = m+1
        return left
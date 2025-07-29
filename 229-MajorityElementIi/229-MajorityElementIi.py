# Last updated: 7/29/2025, 5:48:25 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = 0, 0
        n1, n2 = None, None
        thresh = len(nums)//3
        result = []
        
        if not nums :
            return []
        
        for num in nums :
            if c1 == 0 and num!=n2: # can exclude this if ordered later 
                n1 = num
                c1+=1
            elif c2 == 0 and num!=n1:
                n2 = num
                c2+=1
            elif n1 == num :
                c1+=1
            elif n2 == num :
                c2+=1
            else :
                c1-=1
                c2-=1
        
        c1, c2 = 0, 0
        for num in nums :
            if n1 == num :
                c1+=1
            elif n2 == num :
                c2+=1
        
        if c1 > thresh :
            result.append(n1)
        if c2 > thresh  :
            result.append(n2)
        
        return sorted(result)


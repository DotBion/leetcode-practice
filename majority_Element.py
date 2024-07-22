class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        l=0
        for i in nums :
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            
        for i in d.keys() :
            if d[i] > l:
                l=d[i]
                pos = i
        return pos

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        d ={}
        ls = len(s)
        lt = len(t)
        if lt!=ls :
            return False
        
        for i in s :
            if i in d :
                d[i]+=1
            else :
                d[i]=1
        
        for i in t :
            if i in d:
                d[i]-=1
            else :
                return False
        v = d.values()
        for i in v :
            if i != 0 :
                return False
        return True




            

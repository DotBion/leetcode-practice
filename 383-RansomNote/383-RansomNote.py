# Last updated: 7/29/2025, 5:48:18 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        for i in magazine :
            if i not in d1:
                d1[i]=1
            else :
                d1[i]+=1
        
        for i in ransomNote :
            if i not in d1 or d1[i]<=0 :
                return False
            else :
                d1[i]-=1
        return True
                
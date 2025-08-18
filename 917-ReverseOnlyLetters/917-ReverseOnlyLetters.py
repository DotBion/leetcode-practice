# Last updated: 8/18/2025, 7:51:10 AM
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s)-1
        slist = list(s)
        res = []
        print(s[left].isalpha())
        while left<right :
            if s[left].isalpha() != True :
                left+=1
            elif s[right].isalpha() != True :
                right-=1
            elif s[left].isalpha() == s[right].isalpha() :
                slist[left],slist[right] = slist[right], slist[left]
                left+=1
                right-=1
        return "".join(slist)
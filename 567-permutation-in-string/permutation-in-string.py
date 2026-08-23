class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1>l2:
            return False
        ws = l1 
        s1 = "".join(sorted(s1))
        start = 0
        while start <= l2 :
            ss2 = "".join(sorted(s2[start:start+ws]))
            if ss2 == s1 :
                return True
            start+=1
        return False
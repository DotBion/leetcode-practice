# Last updated: 5/28/2025, 8:53:30 AM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        count=0
        while i<len(s) and j<len(t) :
            if s[i] == t[j] :
                count+=1
                i+=1
            j+=1
        if count == len(s):
            return True
        return False
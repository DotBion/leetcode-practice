class Solution:  
    def romanToInt(self, s: str) -> int:
        getIntVal = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(s)
        val = getIntVal[s[0]]
        prev = getIntVal[s[0]]
        for i in range(1,l):
            p = getIntVal[s[i]]
            if prev < p :
                val = val - 2*prev
            prev = p
            val = val + p
        return val

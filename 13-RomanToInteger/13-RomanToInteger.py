# Last updated: 7/29/2025, 5:48:43 PM
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


        # for i in range(l-1):
        #     if s[i] == 'I':
        #         if s[i+1] == 'V' or s[i+1] == 'X':
        #             val = val + getIntVal[s[i+1]] - getIntVal[s[i]]
        #             i=i+1
        #         else :
        #             val = val + getIntVal[s[i]]
        #     elif s[i] == 'X':
        #         if s[i+1] == 'L' or s[i+1] == 'C':
        #             val = val + getIntVal[s[i+1]] - getIntVal[s[i]]
        #             i=i+1
        #         else :
        #             val = val + getIntVal[s[i]]
        #     elif s[i] == 'C':
        #         if s[i+1] == 'D' or s[i+1] == 'M':
        #             val = val + getIntVal[s[i+1]] - getIntVal[s[i]]
        #             i=i+1
        #         else :
        #             val = val + getIntVal[s[i]]
        #     else :
        #         val = val + getIntVal[s[i]]

        return val
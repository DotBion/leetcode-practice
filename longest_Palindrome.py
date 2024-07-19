class Solution:
    def longestPalindrome(self, s: str) -> int:
        #s = s.lower()
        d = {}
        f=0
        l=0
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d.keys():
            l = l + d[i]
            if d[i]%2 == 1:
                f=1
                l=l-1
        return l+f

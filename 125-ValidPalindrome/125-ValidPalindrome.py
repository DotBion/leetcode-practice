# Last updated: 7/29/2025, 5:48:31 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = s.strip()
        str = ""
        for i in s :
            if i.isalnum() :
                str = str + i
        str = str.casefold()
        s = str
        l = len(s)
        for i in range(l):
            if s[i] != str[l - i-1] :
                return False
        return True
# Last updated: 7/29/2025, 5:48:19 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        #two pass approach
        # stack = []
        # result = ""
        
        # for i in s :
        #     if i in vowels :
        #         stack.append(i)
        # for i in s:
        #     if i in vowels :
        #         result += stack.pop()
        #     else :
        #         result += i
        # return result
        
        #one pass approach
        s = list(s)
        i,f = 0, len(s)-1
        while i<f :
            while s[i] not in vowels and i<f :
                i+=1
            while s[f] not in vowels and i<f :
                f-=1
            if i<f :
                s[i],s[f] = s[f],s[i]
                i+=1
                f-=1
        return "".join(s)


# Last updated: 7/29/2025, 5:48:41 PM
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        hm = {'(':')','{':'}','[':']'}
        for i in s:
            if i in ['(','[','{'] :
                stack.append(hm[i])
            elif i in [')','}',']']:
                if len(stack) == 0 :
                    return False
                elif i != stack.pop():
                    return False
            #elif len(stack)!=0 and i == stack[-1]:
                #stack.pop()
        if len(stack) == 0 :
            return True
        return False

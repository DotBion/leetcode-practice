class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []
        for i in s :
            if i == '#':
                if len(sstack)>0:
                    sstack.pop()
            else :
                sstack.append(i)
        for i in t :
            if i == '#':
                if len(tstack)>0:
                    tstack.pop()
            else :
                tstack.append(i)
        if len(tstack) == len(sstack) :
            for i in range(len(tstack)):
                if tstack.pop() != sstack.pop() :
                    return False
            return True
        return False

            

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l1, l2 = len(s1), len(s2)
        # if l1>l2:
        #     return False
        # ws = l1 
        # s1 = "".join(sorted(s1))
        # start = 0
        # while start <= l2 :
        #     ss2 = "".join(sorted(s2[start:start+ws]))
        #     if ss2 == s1 :
        #         return True
        #     start+=1
        # return False
        #TC: O(nmlogm)

        c1 = [0]*26
        c2 = [0]*26
        l1, l2 = len(s1), len(s2)
        if l1>l2 :
            return False
        ref = ord('a')
        for ch in s1 :
            c1[ord(ch) - ref] += 1
        for i in range(l1) :
            c2[ord(s2[i]) - ref] += 1
        if c1 == c2 :
            return True
        left = 0
        for right in range(l1,l2) :
            #remove from left
            c2[ord(s2[left]) - ref] -= 1
            left+=1
            #add right val
            c2[ord(s2[right]) - ref] += 1
            if c1 == c2 :
                return True
        return False
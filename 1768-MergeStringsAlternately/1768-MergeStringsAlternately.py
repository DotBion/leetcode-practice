# Last updated: 5/19/2025, 10:14:49 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        appword = ""
        i=0
        # mn = min(l1,l2)
        while i <l1 or i<l2 :
            if i<l1 :
                appword+=word1[i]
            if i<l2 :
                appword+=word2[i]
            i+=1
        # for i in range(mn) :
        #     appword += word1[i] 
        #     appword += word2[i] 
        # if l1 > l2:
        #     appword += word1[mn:]
        # else :
        #     appword += word2[mn:]
        return appword
            
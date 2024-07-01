class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        ls =[]
        lt =[]
        l = len(s)
        try:
            for i in range(l):
                ls.append(s[i])
                lt.append(t[i])
        except IndexError :
            return False #unequal string so anagram not possible
        
        for i in ls:
            if i in lt :
                lt.remove(i)
            ls.remove(i)




            

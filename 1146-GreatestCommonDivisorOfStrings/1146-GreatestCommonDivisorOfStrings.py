# Last updated: 7/29/2025, 5:48:13 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        root = ""
        result = ""
        for i in range(min(l1,l2),0,-1):
            root = str1[:i]
            #check if the root is a valid root
            if l1%i or l2 % i :
                #invalid root since it will not complete one fo the strings
                root = "" #reset root
            else : 
                #check if the the root actually reproduces l1 and l2
                if (l1//i)*root == str1 and (l2//i)*root == str2 :
                    result = root
                    break
                else :
                    root = ""
        return result
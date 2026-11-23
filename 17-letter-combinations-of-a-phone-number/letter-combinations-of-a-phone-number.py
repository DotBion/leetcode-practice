class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        hashmap = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def backtrack(i, currS) :
            #bc : if i >=
            if len(currS) == len(digits) :
                res.append(currS)
                return
            #we havent finished processing
            for c in hashmap[digits[i]] :
                #for every single character bruteforce
                backtrack(i+1, currS+c)
        if digits :
            backtrack(0,"")
        return res
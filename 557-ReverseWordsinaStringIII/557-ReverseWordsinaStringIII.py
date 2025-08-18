# Last updated: 8/18/2025, 7:32:01 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = []
        space_i = -1

        for i in range(len(s)) :
            if i==len(s)-1 or s[i]==' ':
                rev_i = i if i == len(s) - 1 else i-1 #if last chr then i-1, if space then prev el
                while rev_i > space_i :
                    result.append(s[rev_i])
                    rev_i -= 1
                if i!=len(s) - 1 :#not end of string
                    result.append(' ')
                space_i = i
        return "".join(result)

        
        
        # words = s.split() #O(n)
        # #print(words)
        # for i in range(len(words)):
        #     #print(words[i])
        #     words[i] = words[i][::-1]
        # #print(words)
        # return ' '.join(words) #O(n)



        #used this since string immutable in python hence better convert to list and then reconvert to string
        # sent = [' ']
        # ans = []
        # temp = []
        # for i in s :
        #     sent.append(i)
        # print(sent)
        # for i in range(len(sent)-1,-1,-1) :
        #     if sent[i] == ' ':
        #         ans.append("".join(temp))
        #         ans.append(' ')
        #         temp = []
        #     else :
        #         temp.append(sent[i])
        # temp = []
        # for i in range(len(ans)-1,-1,-1) :
        #     temp.append(ans[i])
        # #print(len((" ".join(temp)).strip()))
        # return ("".join(temp)).strip()

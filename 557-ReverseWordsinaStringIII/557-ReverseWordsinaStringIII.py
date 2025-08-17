# Last updated: 8/17/2025, 10:43:55 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        sent = [' ']
        ans = []
        temp = []
        for i in s :
            sent.append(i)
        print(sent)
        for i in range(len(sent)-1,-1,-1) :
            if sent[i] == ' ':
                ans.append("".join(temp))
                ans.append(' ')
                temp = []
            else :
                temp.append(sent[i])
        temp = []
        for i in range(len(ans)-1,-1,-1) :
            temp.append(ans[i])
        #print(len((" ".join(temp)).strip()))
        return ("".join(temp)).strip()

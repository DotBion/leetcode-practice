# Last updated: 8/19/2025, 7:44:42 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chi = -1
        for i in range(len(word)) :
            if ch == word[i] :
                chi = i
                break
        res = []
        for i in range(chi,-1,-1) :
            res.append(word[i])

        ans = "".join(res) + word[chi+1:]
        return ans

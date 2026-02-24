# Last updated: 2/24/2026, 12:41:10 AM
1class Solution:
2    def makeGood(self, s: str) -> str:
3        #characters = list(s)
4        greatString = [s[0]]
5        if len(s) < 2 :
6            return s 
7        for i in range(1, len(s)) :
8            if greatString :
9                if abs(ord(s[i]) - ord(greatString[-1])) == 32 :
10                    greatString.pop()
11                else :
12                    greatString.append(s[i])
13            else :
14                greatString.append(s[i])
15
16        return "".join(greatString)
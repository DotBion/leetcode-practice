# Last updated: 2/24/2026, 12:06:01 AM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        currs = ""
5        path = path + "/" #to process the last currs
6        for i in path:
7            if i == "/" :
8                if currs == ".." :
9                    if stack:
10                        stack.pop()
11                elif currs != "." and currs!="":
12                    stack.append(currs)
13                currs = ""
14            else :
15                currs = currs + i
16        print(stack)
17        result = "/" + "/".join(stack)
18        return result
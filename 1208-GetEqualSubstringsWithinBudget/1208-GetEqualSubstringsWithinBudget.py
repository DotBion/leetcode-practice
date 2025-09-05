# Last updated: 9/5/2025, 11:23:06 AM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = []
        for i in range(len(s)) :
            cost.append(abs(ord(s[i])-ord(t[i])))
        
        left = 0
        currcost = 0
        maxlen = 0

        for right in range(len(s)) :
            currcost += cost[right]

            #shrink window until currcost is valid i.e. less than= maxcost
            while currcost > maxCost :
                currcost -= cost[left]
                left += 1
            
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
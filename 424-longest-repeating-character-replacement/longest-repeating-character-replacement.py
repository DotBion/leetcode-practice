from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lols = 0
        left = right = 0
        c = Counter()
        for right in range(len(s)) :
            #extra chars = currentwindo - maxfreq of a letter <= k
            c[s[right]]+=1
            maxfreq = max(c.values())
            #check if the window is not valid
            while right-left+1 - maxfreq > k :
                c[s[left]] -= 1
                left+=1
                maxfreq = max(c.values())
            #at this point we always ensure a valid window
            lols = max(lols, right - left +1)
        return lols
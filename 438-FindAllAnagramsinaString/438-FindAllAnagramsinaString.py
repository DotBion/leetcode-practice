# Last updated: 10/6/2025, 6:42:36 PM
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sort the p in ascending
        #take slices of len(p) from s
        #sort the slice
        #check slice equal sorted p
        #store indices
        result = []
        sp = "".join(sorted(p))
        
        for i in range(0,len(s)) :
            if i+len(p) > len(s) :
                break
            s_sliced = "".join(sorted(s[i:i+len(p)]))
            if s_sliced == sp :
                result.append(i)
        return result

            


# Last updated: 9/5/2025, 11:37:13 AM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0]
        for i in range(len(gain)) :
            alts.append(alts[i]+gain[i])
        return max(alts)
# Last updated: 5/19/2025, 9:50:52 PM
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        l = []
        l.append(words[0])
        for i in range(1,len(groups)):
            if groups[i]!=groups[i-1] :
                l.append(words[i])
        return l

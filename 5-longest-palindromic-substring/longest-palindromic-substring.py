class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_len = 0
        beststr = ""

        def helper(l, r):
            nonlocal best_len, beststr
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best_len:
                    best_len = r - l + 1      # was r + l - 1
                    beststr = s[l:r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i, i)          # odd-length center
            helper(i, i + 1)      # even-length center
        return beststr            # after the loop, using beststr (not res)
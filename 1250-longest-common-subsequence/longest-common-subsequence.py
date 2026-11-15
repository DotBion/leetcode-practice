class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #initialize a 2D dp with an extra col and row to handle edge cases
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

        #bottomup
        for i in range(len(text1)-1,-1,-1) :
            for j in range(len(text2)-1,-1,-1) :
                #check if the strings match
                if text1[i] == text2[j] :
                    #move forward the diagonal
                    dp[i][j] = 1 + dp[i+1][j+1]
                else :
                    #check the right and lower for the max value
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])

        return dp[0][0]
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(n) :
            if n in memo : return memo[n]
            if n<=2 :
                return n
            memo[n] = ways(n-1) + ways(n-2)
            return memo[n]
        return ways(n)
        
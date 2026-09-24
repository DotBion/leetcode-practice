class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using combinatorics
        #total moves = m-1 + n-1 = m+n-2
        num = 1
        for i in range(m+n-2,0,-1):
            num *= i
        d1 = d2 = 1
        for i in range(m-1,0,-1) :
            d1*=i
        for i in range(n-1,0,-1) :
            d2*=i
        return int(num/(d1*d2))
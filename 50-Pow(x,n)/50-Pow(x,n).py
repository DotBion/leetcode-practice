# Last updated: 7/25/2025, 7:23:17 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calcPow(x, n) :
            if x == 0 :
                return 0
            if n == 0 :
                return 1

            res = calcPow (x, n//2)
            res = res*res

            if n%2 == 1 :
                res = res*x

            return res
        
        ans = calcPow(x, abs(n))
        if n >=0 :
            return ans
        
        return 1/ans
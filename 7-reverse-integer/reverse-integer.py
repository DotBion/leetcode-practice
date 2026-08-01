class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        s = 0
        range = 2**31
        if x < 0 :
            neg = 1
            x = -x
        
        while x>0 :
            r = x%10
            s = s*10 + r
            x = x//10

        if neg :
            s = -s
            if s < -range :
                return 0
            else :
                return s
        
        if s > range - 1 :
            return 0
        return s
# Last updated: 7/29/2025, 5:48:36 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        #do maths
        #n=1 : 1
        #n=2 : 2; 1+1,2
        #n=3 : 3; 3 1s,2+1,1+2
        #n=4 : 5; 4 1s,2+2,1+1+2(3!/2!=3)
        #n=5 : 8; 5 1s,2+2+1(3),2+1+1+1(4!/3!=4), 
        #n=6 : 13; Fibonacci Series ...
        # if n==1:
        #     return 1
        # elif n==2:
        #     return 2
        # else :
        #     return self.climbStairs(n-2) + self.climbStairs(n-1)
        a=1
        b=2
        if n==1:
            return 1
        elif n==2:
            return 2
        else :
            for i in range(3,n+1):
                c=a+b
                a=b
                b=c
            return c


        

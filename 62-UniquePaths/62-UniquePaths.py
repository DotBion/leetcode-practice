# Last updated: 7/29/2025, 5:48:36 PM
from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #easiest - combinaitons logic
        total_spaces = m+n-2
        small = min(m,n) - 1
        num = 1
        den = 1
        for i in range(small,0,-1) :
            #print(i)
            num = num * total_spaces
            den = den * i
            total_spaces-=1
        return num//den
        

        #graph approaches - naive and DP
        #O(m*n) TLE
        # hm = defaultdict(lambda: -1)
        # def find_path(self, i: int,j: int) :
        #     if i>m-1 or j>n-1 :
        #         return 0
        #     elif i==m-1 and j==n-1 :
        #         return 1
        #     elif hm[i,j] != -1 :
        #         return hm[i,j]
        #     return find_path(self,i+1,j) + find_path(self,i,j+1)
        # return find_path(self,0,0)
        
        #O(2^(m*n)) TLE
        # def find_path(self, i: int,j: int) :
        #     if i>m-1 or j>n-1 :
        #         return 0
        #     elif i==m-1 and j==n-1 :
        #         return 1
        #     return find_path(self,i+1,j) + find_path(self,i,j+1)
        # return find_path(self,0,0)

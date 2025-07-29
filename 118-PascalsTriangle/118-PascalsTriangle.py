# Last updated: 7/29/2025, 5:48:33 PM
class Solution:
    def getCombination(self,n,r):
        dividend=1
        divisor = 1
        for i in range(r,0,-1) :
            dividend = dividend*n
            n-=1
            divisor *=  i
        return dividend//divisor
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows) :
            ll=[]
            for j in range(i+1) :
                #compute nCr = iCj
                ij = self.getCombination(i,j)
                ll.append(ij)
            ans.append(ll)
        return ans
    
    
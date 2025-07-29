# Last updated: 7/29/2025, 5:48:20 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        list = []
        for temp in range(n+1):
            i = temp
            ones = 0
            while i!=0 :
                if i%2 == 1 :
                    ones= ones+1
                i=i//2
            list.append(ones)
        return list
        

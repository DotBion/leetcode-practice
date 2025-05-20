# Last updated: 5/20/2025, 7:35:44 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = flowerbed[0]
        next = flowerbed[0]
        #checking triplets for 000 takes care of initial start like 00 but not ending x00
        for i in range(len(flowerbed)-1):
            next = flowerbed[i+1]
            if flowerbed[i] == 0 and prev == 0 and next == 0: #flowerbed[i] == 0 and
                n-=1
                flowerbed[i] = 1
            prev = flowerbed[i]
        
        #takes care of ...00 endings
        if prev==0 and next==0 :
            n-=1

        if n>0:
            return False
        else :
            return True

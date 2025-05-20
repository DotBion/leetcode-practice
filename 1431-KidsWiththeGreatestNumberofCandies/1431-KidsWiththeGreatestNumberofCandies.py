# Last updated: 5/20/2025, 7:06:41 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxcandies = max(candies)
        for i in candies :
            if i+extraCandies >= maxcandies :
                result.append(True)
            else :
                result.append(False)
        return result

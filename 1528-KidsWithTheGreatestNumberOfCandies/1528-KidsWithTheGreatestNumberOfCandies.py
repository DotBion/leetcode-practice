# Last updated: 7/29/2025, 5:48:11 PM
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

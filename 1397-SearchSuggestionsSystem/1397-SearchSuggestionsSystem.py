# Last updated: 7/29/2025, 5:48:12 PM
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        max = 3
        products.sort()
        #print(products)
        suggestion = []
        for i in range(1,len(searchWord)+1) :
            s = searchWord[0:i]
            stemp = []
            k=0
            for p in products :
                if p.startswith(s) and k<max:
                    stemp.append(p)
                    k+=1
            suggestion.append(stemp)
        return suggestion
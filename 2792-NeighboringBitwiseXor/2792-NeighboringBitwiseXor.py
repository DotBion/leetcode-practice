# Last updated: 7/29/2025, 5:48:10 PM
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        one = 1
        zero = 0
        original=[]
        
        if one^zero == derived[0] :
            original.append(zero)
            original.append(one)
        else :
            original.append(zero)
            original.append(zero)

        for i in range(1,len(derived)-1) :
            #if derived[i] == 1 and original[i]^0 == derived[i]:
            if original[i]^0 == derived[i]:
                original.append(zero)
            #elif derived[i] == 1 and original[i]^1 == derived[i]:
            if original[i]^1 == derived[i]:
                original.append(one)
            #elif derived[i] == 0 and original[i]^0 == derived[i]:
            #    original.append(zero)
            #elif derived[i] == 0 and original[i]^1 == derived[i]:
            #    original.append(one)
        
        if original[0]^original[len(derived)-1] == derived[len(derived)-1] :
            return True
        else:
            return False

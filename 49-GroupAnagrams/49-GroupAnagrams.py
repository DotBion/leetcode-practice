class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        temp = strs[0]
        temp = str(''.join(sorted(temp)))
        hm[temp] = [0]
        result = []
        for i in range(1,len(strs)) :
            temp = strs[i]
            temp = ''.join(sorted(temp))
            if temp in hm :
                hm[temp].append(i)
            else:
                hm[temp]=[i]
        for k in hm :
            temp = []
            for i in hm[k] :
                temp.append(strs[i])
            result.append(temp)
        return result
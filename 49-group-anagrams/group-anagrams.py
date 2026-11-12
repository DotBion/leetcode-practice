class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupMap = {}
        res = []
        for i in range(len(strs)) :
            tempstring = "".join(sorted(strs[i]))
            if tempstring in groupMap :
                groupMap[tempstring].append(i)
            else :
                groupMap[tempstring] = [i]
        #print(groupMap)
        for k,v in groupMap.items() :
            #print(k,v)
            temp = []
            for i in v :
                temp.append(strs[i])
            res.append(temp)
        return res
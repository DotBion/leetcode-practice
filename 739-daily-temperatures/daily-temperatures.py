class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        s =[]
        res = [0]*len(temperatures)
        for i in range(len(temperatures)) :
            while s and temperatures[i] > temperatures[s[-1]] :
                topindex = s.pop()
                res[topindex] = i - topindex
            s.append(i)
        return res


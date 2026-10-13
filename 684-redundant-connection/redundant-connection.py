class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [0]*(len(edges)+1)
        def findup(u) :
            if u == par[u]:
                return u
            # return findup(par[u]) #O(logN)
            par[u] = findup(par[u])
            return par[u] #O(1)
        def unionbyrank(u, v) :
            up_u, up_v = findup(u), findup(v)
            if up_u == up_v :
                return True #already connected means a cycle exists
            if rank[up_u] > rank[up_v] :
                par[up_v] = up_u
            elif rank[up_v] > rank[up_u] :
                par[up_u] = up_v
            elif rank[up_v] == rank[up_u] :
                par[up_v] = up_u
                rank[up_u]+=1
            return False
        
        for u,v in edges :
            if unionbyrank(u,v) :
                return [u,v]


            

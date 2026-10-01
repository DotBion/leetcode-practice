class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0
        def dfs(node) :
            for j in range(n) :
                if isConnected[node][j] == 1 and j not in visited :
                    visited.add(j)
                    dfs(j)
        for i in range(n) :
            if i not in visited :
                count+=1
                #call dfs or bfs : which will explore all nodes inthe tree
                dfs(i) #explore the graph
        return count

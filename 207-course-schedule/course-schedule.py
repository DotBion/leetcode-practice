from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites :
            graph[b].append(a)

        unvisited, visiting, done = 0,1,2
        state = [unvisited]*numCourses
        def dfs(node) :
            #check cycle
            if state[node] == visiting :
                return False
            if state[node] == done :
                return True

            state[node] = visiting
            for neighbor in graph[node] :
            #check all the neighbours if reachable or cycle exists
                if not dfs(neighbor) : #vissiting
                    return False
            state[node] = done
            return True
                
        for c in range(numCourses) :
            if not dfs(c) :return False
        return True



            
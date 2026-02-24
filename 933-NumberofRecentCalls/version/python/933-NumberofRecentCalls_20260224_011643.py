# Last updated: 2/24/2026, 1:16:43 AM
1class RecentCounter:
2
3    def __init__(self):
4        self.q = deque()
5        self.count = 0
6
7    def ping(self, t: int) -> int:
8        self.q.append(t)
9        self.count+=1
10
11        while self.q and self.q[0] < t-3000 :
12            self.q.popleft()
13            self.count -=1
14
15        return self.count
16
17
18# Your RecentCounter object will be instantiated and called as such:
19# obj = RecentCounter()
20# param_1 = obj.ping(t)
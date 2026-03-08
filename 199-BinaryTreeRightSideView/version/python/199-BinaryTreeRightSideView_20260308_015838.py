# Last updated: 3/8/2026, 1:58:38 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        q = collections.deque([root])
11
12        while q :
13            qright = None
14            qlen = len(q)
15            
16            for i in range(qlen) :
17                node = q.popleft()
18                if node :
19                    qright = node
20                    q.append(node.left)
21                    q.append(node.right)
22            if qright :
23                res.append(qright.val)
24        return res
25
26                
27
28
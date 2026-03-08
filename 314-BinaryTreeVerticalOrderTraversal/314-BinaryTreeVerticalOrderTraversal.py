# Last updated: 3/8/2026, 11:07:44 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        q = collections.deque([(root, 0)])
10        columnTable = defaultdict(list)
11
12        while q :
13            node, column = q.popleft()
14
15            if node is not None :
16                #add to the map
17                columnTable[column].append(node.val)
18
19                q.append((node.left, column - 1))
20                q.append((node.right, column+1))
21
22        print(columnTable)
23        res = []
24        for i in sorted(columnTable.keys()) :
25             res.append(columnTable[i])
26
27        return res
28
29
30        
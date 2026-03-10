# Last updated: 3/10/2026, 7:44:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        q = collections.deque([root])
11        parentMap = {}
12        parentMap[root] = None
13        #create upward link / parentmap
14        while q :
15            qlen = len(q)
16            for i in range(qlen) :
17                node = q.popleft()
18                if node :
19                    left = node.left
20                    right = node.right
21                    if left :
22                        parentMap[left] = node
23                        q.append(left)
24                    if right :
25                        parentMap[right] = node
26                        q.append(right)
27        #print(parentMap)
28        q.append(target)
29        visited = []
30        distance = k
31        res = []
32        while q and distance>0:
33            qlen = len(q)
34            distance = distance-1
35            for i in range(qlen) :
36                node = q.popleft()
37                if node :
38                    visited.append(node)
39                    # distance = distance-1
40                    if node.right not in visited :
41                        q.append(node.right)
42                    if node.left not in visited :
43                        q.append(node.left)
44                    if parentMap[node] not in visited :
45                        q.append(parentMap[node])
46        for i in q :
47            if i:
48                res.append(i.val)
49        return res
50
51
52        
53        
54        
55        #def findParent(currentNode: TreeNode, target: TreeNode) :
56        #     #print(root)
57        #     if currentNode == None :
58        #         return None
59        #     if currentNode.left == target or currentNode.right == target :
60        #         return currentNode
61        #     #search left subtree
62        #     result = findParent(currentNode.left, target)
63        #     if result :
64        #         return result
65        #     #search right subttreee
66        #     result = findParent(currentNode.right, target)
67        #     if result :
68        #         return result
69        #     return None
70
71        # targetP = findParent(root, target)
72        # #print("tp",targetP.val)
73        # #will pass the target node as root here ot check it subtrees
74        # if targetP :
75        #     def dfs(root: TreeNode, k: int) :
76        #         a = []
77        #         if root == None :
78        #             return
79        #         if k == 0 :
80        #             return root.val
81        #         if root.right is not None :
82        #             a.append(dfs(root.right, k-1))
83        #         if root.left is not None :
84        #             a.append(dfs(root.left, k-1))
85        #         return a
86
87        #     result = dfs(target, k)
88        #     print("r",result)
89        #     #check the parent's other child subtree
90        #     if targetP.left == target :
91        #         result.append(dfs(targetP.right,k))
92        #     elif targetP.right == target:
93        #         result.append(dfs(targetP.left,k))
94
95        #     return [item for sublist in result for item in sublist]
96        # return []
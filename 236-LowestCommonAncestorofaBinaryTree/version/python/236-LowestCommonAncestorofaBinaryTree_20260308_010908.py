# Last updated: 3/8/2026, 1:09:08 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if root == None or root.val == q.val or root.val == p.val :
11            return root
12        
13        left = self.lowestCommonAncestor(root.left, p, q)
14        right = self.lowestCommonAncestor(root.right, p, q)
15
16        if not left :
17            return right
18        elif not right :
19            return left 
20        else : #left and right are not null
21            return root
22
23            
24            
25
26
27
28
# Last updated: 3/7/2026, 11:37:56 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: Optional[TreeNode]) -> int:
9        def dfs(curr, nums) :
10            #if node null
11            if not curr :
12                return 0
13            nums = nums*10 + curr.val
14            #if leaf node
15            if not curr.left and not curr.right :
16                return nums
17            #not a leaf node - so check left subtree and right subtree
18            return dfs(curr.left, nums) + dfs(curr.right, nums)
19        
20        return dfs(root, 0)
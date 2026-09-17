# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #check the ls and rs if they have p and q
        #whichever has both is the answer
        
        #i check the subtrees
        def dfs(node) :
            if not node :return node
            if node == p or node == q:
            #we find either, then we return this val
                return node
            ls = dfs(node.left)
            rs = dfs(node.right)
            #check if both are not none
            if ls and rs :
                #this is my answer
                return node
            #if either of them has a val return it
            return ls or rs
        return dfs(root)
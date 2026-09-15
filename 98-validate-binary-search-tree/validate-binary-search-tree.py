# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        #root can bve between -infi to +infi
        #ls can be between -infi and 2
        #rs can be between 2 and +infi
        #so going to ls limits the ub and rs limits the lb with the root of it
        pi = float("inf")
        ni = float("-inf")
        def dfs(node, lb, ub) :
            if not node:
            #if node/child dne then there's nothing to check validity, hence its valid so return True
                return True
            #check if current node valid
            if node.val<=lb or node.val>=ub :
                return False
            #if valid then check its ls and rs
            ls = dfs(node.left, lb, node.val)
            rs = dfs(node.right, node.val, ub)
            #return true or false based on if the ls and rs are valid
            return ls and rs
        
        return dfs(root, ni, pi)
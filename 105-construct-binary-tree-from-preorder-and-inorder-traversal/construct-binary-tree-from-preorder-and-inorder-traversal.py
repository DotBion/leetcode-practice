# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        idx = {val: i for i, val in enumerate(inorder)}
        def maketree(pre_start, in_start, in_end):
            if in_start > in_end :
                return None
            root_val = preorder[pre_start]
            m = idx[root_val]
            left_size = m - in_start
            node = TreeNode(root_val)
            node.left = maketree(pre_start + 1, in_start, m-1)
            node.right = maketree(pre_start + 1 + left_size,  m + 1,    in_end)
            return node
        return maketree(0, 0, len(inorder) - 1) 
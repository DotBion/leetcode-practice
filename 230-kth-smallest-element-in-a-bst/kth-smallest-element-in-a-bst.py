# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        n = 0
        stack = []
        curr = root
        val = []
        while curr or stack:
            while curr :
                stack.append(curr)
                #val.append(curr.val)
                curr = curr.left
            #print(val)
            #now curr is none, i.e the last element is the stack top and the smallest element
            curr = stack.pop()
            n += 1
            if n==k :
                return curr.val
            #check right subtree
            curr = curr.right
        #since k<nodes in tree we dont need a return here
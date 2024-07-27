# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        c=0
        while node!=None :
            c+=1
            node=node.next
        mid = c//2
        node = head
        for i in range(mid):
            node = node.next
        return node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = None
        while head:
            temp = head.next
            head.next = p1
            p1 = head
            head = temp
        return p1


        

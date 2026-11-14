# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0,head)
        l = 0 
        curr = head 
        while curr!=None :
            curr = curr.next
            l+=1
        curr = dummy
        for i in range(l-n) :
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        for i in range(n) :
            right = right.next
        #left and right are at a distance n
        #now iterate until right hits end so left will be a node prior to the ndoe to delete. prior since we introduced dummy. else we would be on the node to be deleted but wouldnt be able to since we need to link the prev node to the next of teh node to be deleted.

        while right!=None :
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
# Last updated: 7/29/2025, 5:48:30 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None :
            return False
        slow = head
        fast = head.next
        while fast != slow :
            if fast == None or fast.next == None or fast.next.next==None or slow == None or slow.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
            
        return True
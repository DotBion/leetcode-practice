# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head
        carry = 0
        sum = 0
        while l1 or l2 or carry:
            if l1 :
                sum+=l1.val
                l1 = l1.next
            if l2 :
                sum+=l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            sum = sum%10
            curr.next = ListNode(sum)
            sum = 0
            curr = curr.next
        return dummy_head.next
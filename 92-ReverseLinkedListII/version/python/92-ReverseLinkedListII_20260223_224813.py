# Last updated: 2/23/2026, 10:48:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8    
9        dummy = ListNode(0, head)
10
11        prev, curr = dummy, head
12        for i in range(left-1) :
13            prev, curr = prev.next, curr.next
14        
15        pl = prev
16        prev = None
17        for i in range(right - left + 1) :
18            temp = curr.next
19            curr.next = prev
20            prev = curr
21            curr = temp
22
23        pl.next.next = curr
24        pl.next = prev
25        return dummy.next
26
27
28
# Last updated: 2/23/2026, 10:16:54 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev = None
9        current = head
10        while current :
11            temp = current.next
12            current.next = prev
13            prev = current
14            current = temp
15        return prev
16
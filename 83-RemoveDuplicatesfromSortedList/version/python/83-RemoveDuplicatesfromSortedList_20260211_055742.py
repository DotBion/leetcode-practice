# Last updated: 2/11/2026, 5:57:42 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        p1 = head
9        p2 = head
10        while p1!=None and p1.next != None:
11            p2 = p1.next
12            #find the next non-duplicate
13            while p2!=None and p2.val == p1.val :
14                p2 = p2.next
15            #link the non-duplicate node
16            p1.next = p2
17            p1 = p1.next
18        return head
19
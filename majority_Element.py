class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = head
        fp = head

        while fp is not None and fp.next is not None:
            sp= sp.next
            fp = fp.next.next

        return sp

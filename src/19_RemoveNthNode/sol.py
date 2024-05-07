# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = None
        index = 0
        while p1.next:
            p1 = p1.next
            index += 1
            if index >= n:
                if p2 is None:
                    p2 = head
                else:
                    p2 = p2.next
        if p2 is None:
            return head.next
        else:
            p2.next = p2.next.next
        return head

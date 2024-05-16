# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # result for list with zero or one node
            return head
        
        res = ListNode()
        res.next = head

        cur = res
        while cur.next and cur.next.next:
            # now we have cur -> first -> second -> next
            first = cur.next
            second = cur.next.next

            # swap cur -> second -> first -> next
            first.next = second.next
            second.next = first
            cur.next = second

            # next step
            cur = cur.next.next

        return res.next

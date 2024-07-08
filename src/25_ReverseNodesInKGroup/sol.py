# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we length list is less than k or no
        cur = head
        temp = 0
        while cur:
            cur = cur.next
            temp += 1
            if temp == k:
                break

        if temp != k:
            return head
		        
				
        # Reverse the link list
        prv = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
		# And `cur` is the next pointer in original linked list order
        head.next = self.reverseKGroup(cur, k)
        return prv
    

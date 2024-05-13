# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mapped = {}
        for l in lists: # Add all of items in a dictionary
            while l is not None:
                if l.val not in mapped:
                    mapped[l.val] = []
                mapped[l.val].append(l.val)
                
                l = l.next

        keys = sorted(mapped.keys()) # sort dictionary keys 
        if len(keys) == 0:
            return
        tail = None
        head = None
        print()
        for i in keys: # loop over all items and make the list node
            for item in mapped[i]:
                temp = ListNode(val=item)
                if tail is None:
                    tail = temp
                    head = tail # save the head to return it
                else:
                    tail.next = temp
                    tail = tail.next
        return head

        

        


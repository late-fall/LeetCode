# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = temp = nxt = head
        i = 0
        while temp:
            i += 1
            temp = temp.next
        for j in range(k % i):
            nxt = nxt.next
        while nxt.next:
            curr = curr.next
            nxt = nxt.next
        nxt.next = head
        new_head = curr.next
        curr.next = None
        return new_head
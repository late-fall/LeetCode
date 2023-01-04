# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        even_start = head.next
        even = head.next
        odd = head
        while even.next:
            odd.next = odd.next.next
            odd = odd.next
            if odd.next is None:
                even.next = None
                break
            
            even.next = even.next.next
            even = even.next
        odd.next = even_start
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            if head.val == val:
                head = None
            else:
                return head
        while head and head.val == val:
            head = head.next
        point = head
        while point and point.next:
            if point.next.val == val:
                point.next = point.next.next
                continue
            point = point.next
        if point and point.val == val:
            return None
        return head
            
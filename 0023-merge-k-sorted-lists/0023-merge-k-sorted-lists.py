# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        node = ListNode()
        head = node
        
        for lst in lists:
            while lst:
                heappush(hp, lst.val)
                lst = lst.next
                
        while hp:
            node.next = ListNode(heappop(hp))
            node = node.next
        
        return head.next
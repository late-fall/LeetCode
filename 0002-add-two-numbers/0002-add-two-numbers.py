# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        
        
        # if l1 is None and l2 is None:
        #     if carry == 1:
        #         return ListNode(1, None)
        # elif l1 is None:
        #     carry_over = (l2.val + carry) // 10
        #     value = (l2.val + carry) % 10
        #     l1 = ListNode(value, None)
        #     l1.next = self.addTwoNumbers(None, l2.next, carry_over)
        # elif l2 is None:
        #     carry_over = (l1.val + carry) // 10
        #     l1.val = (l1.val + carry) % 10
        #     l1.next = self.addTwoNumbers(l1.next, None, carry_over)
        # else:
        #     carry_over = (l1.val + l2.val + carry) // 10
        #     l1.val = (l1.val + l2.val + carry) % 10
        #     l1.next = self.addTwoNumbers(l1.next, l2.next, carry_over)
        # return l1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode(-1)
        res, carry = final, 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            cur_sum = l1_val + l2_val + carry
            carry, mod = cur_sum // 10, cur_sum % 10

            final.next = ListNode(mod)
            final = final.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        final.next = ListNode(carry) if carry != 0 else None
        return res.next
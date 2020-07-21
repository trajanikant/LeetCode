# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        hack = ListNode(-1)
        hack.next = head
        new = hack
        while new.next:
            if new.next.val == val:
                new.next = new.next.next
            else:
                new = new.next
        return hack.next

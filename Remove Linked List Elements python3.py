# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, T):
        if not head: return None
        head.next = self.removeElements(head.next, T);
        return head.next if head.val == T else head
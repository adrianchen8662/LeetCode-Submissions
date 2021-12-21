# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = ListNode(0)
        x = root
        while (l1 or l2 or carry):
            if (l1):
                carry += l1.val
                l1 = l1.next
            if (l2):
                carry += l2.val
                l2 = l2.next
            carry,val = divmod(carry,10)
            x.next = ListNode(val)
            x = x.next
        return root.next
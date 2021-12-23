# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = x = ListNode(0)
        
        while list1 and list2:
            if (list1.val < list2.val):
                x.next = ListNode(list1.val)
                list1 = list1.next
            else:
                x.next = ListNode(list2.val)
                list2 = list2.next
            x = x.next
        x.next = list1 or list2
        return root.next
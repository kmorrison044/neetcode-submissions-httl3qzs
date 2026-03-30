# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Trick is to find the last half of the list, reverse the order of the
        # last half of the list, then merge the last half and the first half

        # Find the last half of the list:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the links of the back half of the list:
        last_half = slow.next
        # slow is now going to be the last element, so point it to null:
        prev = slow.next = None
        while last_half:
            tmp = last_half.next
            last_half.next = prev
            prev = last_half
            last_half = tmp
        
        # Merge the last half and the first half
        first_half, last_half = head, prev
        while last_half:
            tmp1, tmp2 = first_half.next, last_half.next
            first_half.next = last_half
            last_half.next = tmp1
            first_half, last_half = tmp1, tmp2
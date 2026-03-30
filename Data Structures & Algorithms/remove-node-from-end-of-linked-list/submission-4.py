# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pass iteration is the trick. O(1) space complexity and O(n)
        # time complexity. First loop counts the number of nodes.
        # second loop goes to the node before the one you want to remove.
        # simply reset the pointer of the node before the one you want to
        # remove to the node after the one you want to remove.

        count = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            count += 1

        targ = count - n
        if targ == 0:
            head = head.next
            return head

        tmp = head
        for _ in range(targ-1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        
        return head



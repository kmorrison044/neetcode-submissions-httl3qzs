# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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



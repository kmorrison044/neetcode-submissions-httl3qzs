# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ### Hash Set method:

        # seen = set()
        # cur = head
        # while cur:
        #     if cur in seen:
        #         return True
        #     seen.add(cur)
        #     cur = cur.next
        # return False


        ### slow/fast pointer method:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
            


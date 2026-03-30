# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Make a dummy node pointing to the head of the list. To reverse groups, you are going to have
    # the last node of the previous group (groupPrev) and the first node of the next group (groupNext).
    # Make a function to grab the last node of the current group (getKth), then since the first node
    # in the current group will be the last, when you do the reverse of the portion, initialize the prev
    # node in the group to kth.next, which will be the first node in the next group. Then
    # reverse a linked list like normal. When done reversing the linked list portion, update
    # groupPrev.next to be the first node in the reversed portion (which is now kth) and update
    # groupPrev itself to be the last node in the reversed portion (which was previously
    # groupPrev.next). This is the most efficient way to solve the problem.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            prev, cur = kth.next, groupPrev.next 
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
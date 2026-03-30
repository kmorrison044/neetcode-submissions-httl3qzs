# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Just add like regular addition. You are starting from the last digit
        # in the number like you would for regular addition by hand, so you
        # can easily manage the carry. Integer division (//) cuts off the decimal
        # so that will be your carry for the next place in the LL. Mod'ing by 10
        # gets the remainder, so that will be your value for the current node in
        # the LL. If the lists are different sizes, just check if there is a node
        # and if not, give it a value of zero, and when updating the pointers,
        # check if they are non-null. If they are, just keep them null.
        # Finally iterate through until l1 and l2 are null and carry is 0 to ensure
        # that if there are no more nodes in either list, and there is still a
        # carry, that is accounted for.
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new num
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
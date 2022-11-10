# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(max(len(l1), len(l2))) time, # O(max(len(l1), len(l2))) space
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        carry = 0
        # Keep adding corresponding places until 
        # both lists are empty and we have no carry 
        # (case when new place is needed as a result of addition)
        while l1  is not None or l2 is not None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            value = l1Val + l2Val + carry
            # Add newly compute sum to the output list
            # Update carry if needed
            carry = value // 10
            tail.next = ListNode(value % 10)
            # Update pointers
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None    

        return dummy.next
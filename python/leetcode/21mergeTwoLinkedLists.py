# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to avoid dealing with edge cases
        dummy = ListNode(val=0, next=None)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # At this point either both lists are None or only one of them is not None
        # Can't be that both are not None
        if list1 is not None:
            tail.next = list1

        if list2 is not None:
            tail.next = list2

        return dummy.next
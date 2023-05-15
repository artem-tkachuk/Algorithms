# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(head):
    # Write your code here.
    curr = head

    while curr is not None and curr.next is not None:
        if curr.next.value == curr.value:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

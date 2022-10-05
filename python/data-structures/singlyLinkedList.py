# Singly Linked List implementation
class SinglyLLNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class SinglyLList:
    __length = 0
    __head = None

    def __init__(self, n: SinglyLLNode):
        self.__head = n
        self.__length = 1

    def find(self, val):
        """
            :param val: value we want to find in the Linked List
            :return: list of tuples with elements being (ptr, index)
                     of every occurance of val in the list
        """
        k = 0

        occurrences = []  # list of all locations where the val if found
        ptr = self.__head

        while ptr is not None:
            if ptr.value == val:
                occurrences.append((ptr, k))
            k += 1
            ptr = ptr.next

        return occurrences

    def insert(self, val, loc=0):
        """
        :param val: value to insert into a Linked List
        :param loc: index at which to insert the value
        :return: None
        """
        assert loc >= 0, "Index can't be negative"

        if loc > self.__length:
            print("Can't insert at this location")
            return None

        prev, ptr = None, self.__head
        for _ in range(loc):
            prev = ptr
            ptr = ptr.next

        newNode = SinglyLLNode(value=val, next=ptr)

        if prev is not None:
            prev.next = newNode
        else:
            self.__head = newNode

        self.__length += 1

    def deleteList(self):
        """
        Delete entire list
        :return: None
        """
        while self.__head is not None:
            ptr = self.__head
            self.__head = ptr.next
            ptr.next = None
            self.__length -= 1

    def delete(self, val):
        """
            Delete all occurances of val from the Linked List
            :param val: value occurences of which are to be deleted from the list
            :return: None
        """
        prev, curr = None, self.__head
        while curr is not None:
            if curr.value == val:
                self.__length -= 1
                # Very start of the list
                if prev is None:
                    self.__head = curr.next
                    curr.next = None
                    curr = self.__head
                # Middle of the list
                else:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next

    def print(self):
        """
        Print the values of all nodes in the linked list
        :return: None
        """
        ptr = self.__head

        while ptr is not None:
            print(ptr.value, end=" -> ")
            ptr = ptr.next
        print("NULL")

    def reverse(self):
        """
        Reverse a Linked List in place
        :return: None
        """
        prev, curr = None, self.__head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.__head = prev

    # Getter methods
    def getHead(self):
        return self.__head

    def getLength(self):
        return self.__length


def testing():
    # Testing
    LL = SinglyLList(SinglyLLNode(value=555, next=None))
    occurrences = LL.find(555)
    print(occurrences)
    LL.insert(1500)
    LL.insert(5500, 2)
    LL.print()
    print(LL.getLength())

    LL2 = SinglyLList(SinglyLLNode())
    LL2.print()

    LL.reverse()
    LL.print()
    LL.reverse()
    LL.print()
    LL.insert(555, 1)
    LL.print()
    LL.delete(555)
    LL.print()
    LL.delete(1500)
    LL.print()
    LL.delete(5500)
    LL.print()

    print("")
    LL2.insert(1000)
    LL2.print()
    LL2.deleteList()
    LL2.print()
    LL2.insert(12)
    LL2.insert(14)
    LL2.print()
    LL2.insert(14, 2)
    LL2.print()
    LL2.delete(14)
    LL2.print()
    print(LL2.getLength())
    print(LL2.getHead())


testing()

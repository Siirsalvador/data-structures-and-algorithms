class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToTail(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)

    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return
        cur = self.head
        prev = cur
        while cur:
            if cur.val == val:
                break
            prev = cur
            cur = cur.next
        prev.next = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print("Node Val : " + str(cur.val))
            cur = cur.next


def main():
    linkedList = LinkedList()
    linkedList.addToTail(1)
    linkedList.addToTail(4)
    linkedList.addToTail(3)
    linkedList.addToTail(2)
    linkedList.addToTail(6)
    linkedList.print_list()
    linkedList.delete(3)
    print()
    linkedList.print_list()


main()

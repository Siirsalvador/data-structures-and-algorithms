from ListNode import ListNode


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        Reverses the passed singly linked list.
        :param head: Head ListNode of the list.
        :return: Head ListNode of the reversed list.
        """
        prev = None
        # nnext = None
        cur = head
        while (cur):
            nnext = cur.next
            cur.next = prev
            prev = cur
            cur = nnext

        return prev

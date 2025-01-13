from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        output = ListNode()
        tail = output

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return output.next


def print_linked_list(head: Optional[ListNode]) -> None:
    """
    The output <__main__.ListNode object at 0x1027f5e80>
    occurs because you are printing the object directly instead of its values.
    This happens when Python’s default string representation (__repr__) is used.
    """
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Test Case
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
response = sol.mergeTwoLists(list1, list2)
print_linked_list(response)

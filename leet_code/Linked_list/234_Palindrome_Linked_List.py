# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
from typing import Optional, Deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numbers = []
        while head.next :
            numbers.append(head.val)
            head = head.next
        numbers.append(head.val)
        return numbers == numbers[::-1]

    def deque(self, head: Optional[ListNode]) -> bool:
        q:Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    def runner(self, head: Optional[ListNode]) -> bool:
        rev = none
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if tast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
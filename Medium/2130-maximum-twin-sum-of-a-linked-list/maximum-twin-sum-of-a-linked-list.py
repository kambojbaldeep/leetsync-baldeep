# Maximum Twin Sum of a Linked List  (#2130)  —  Medium
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Runtime: 70 ms   |   Memory: 50.5 MB
# Language: Python3
# Synced: 2026-08-20 via LeetSync

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        curr = slow
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        head2 = prev
        max_sum = 0
        while head2 is not None:
            max_sum = max(max_sum, head.val + head2.val)
            head = head.next
            head2 = head2.next

        return max_sum
